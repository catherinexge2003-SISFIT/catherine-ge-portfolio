#!/usr/bin/env Rscript

# NHANES 2013-2014: device-measured movement vs self-reported leisure PA

suppressPackageStartupMessages({
  library(haven)
  library(dplyr)
  library(survey)
  library(jsonlite)
})

base <- "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2013/DataFiles"
urls <- list(
  paxday = paste0(base, "/PAXDAY_H.xpt"),
  paq = paste0(base, "/PAQ_H.xpt"),
  demo = paste0(base, "/DEMO_H.xpt"),
  bmx = paste0(base, "/BMX_H.xpt")
)

args_all <- commandArgs(trailingOnly = FALSE)
file_arg <- args_all[grepl("^--file=", args_all)]
script_path <- if (length(file_arg) > 0) {
  normalizePath(sub("^--file=", "", file_arg[[1]]))
} else {
  normalizePath("projects/nhanes-pam-self-report/src/analysis.R")
}
out_dir <- file.path(dirname(dirname(script_path)), "results")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

read_xpt_url <- function(url) {
  tf <- tempfile(fileext = ".xpt")
  download.file(url, tf, mode = "wb", quiet = TRUE)
  on.exit(unlink(tf), add = TRUE)
  read_xpt(tf)
}

clean_special <- function(x) {
  x <- as.numeric(x)
  x[x %in% c(77, 99, 7777, 9999)] <- NA_real_
  x
}

pax_raw <- read_xpt_url(urls$paxday) %>%
  transmute(
    SEQN,
    PAXDAYD = as.numeric(PAXDAYD),
    PAXVMD = as.numeric(PAXVMD),
    PAXMTSD = as.numeric(PAXMTSD),
    PAXWWMD = as.numeric(PAXWWMD),
    PAXSWMD = as.numeric(PAXSWMD),
    PAXNWMD = as.numeric(PAXNWMD),
    PAXUMD = as.numeric(PAXUMD)
  ) %>%
  mutate(
    wear_classified_minutes = PAXWWMD + PAXSWMD,
    mims_per_valid_min = PAXMTSD / PAXVMD
  )

build_pax <- function(valid_min_threshold = 1200, min_days = 4, wear_min_threshold = NULL) {
  x <- pax_raw %>%
    filter(
      !is.na(PAXVMD),
      !is.na(PAXMTSD),
      PAXVMD > 0,
      PAXMTSD >= 0
    )

  if (is.null(wear_min_threshold)) {
    x <- x %>% filter(PAXVMD >= valid_min_threshold)
  } else {
    x <- x %>%
      filter(
        !is.na(wear_classified_minutes),
        wear_classified_minutes >= wear_min_threshold
      )
  }

  x %>%
    group_by(SEQN) %>%
    summarise(
      valid_days = n(),
      mean_mims_per_valid_min = mean(mims_per_valid_min, na.rm = TRUE),
      mean_valid_minutes = mean(PAXVMD, na.rm = TRUE),
      mean_wear_classified_minutes = mean(wear_classified_minutes, na.rm = TRUE),
      .groups = "drop"
    ) %>%
    filter(valid_days >= min_days)
}

paq <- read_xpt_url(urls$paq) %>%
  mutate(
    across(c(PAQ650, PAQ655, PAD660, PAQ665, PAQ670, PAD675), as.numeric),
    PAQ655 = clean_special(PAQ655),
    PAD660 = clean_special(PAD660),
    PAQ670 = clean_special(PAQ670),
    PAD675 = clean_special(PAD675),
    vigorous_met = case_when(
      PAQ650 == 2 ~ 0,
      PAQ650 == 1 & !is.na(PAQ655) & !is.na(PAD660) ~ 8 * PAQ655 * PAD660,
      TRUE ~ NA_real_
    ),
    moderate_met = case_when(
      PAQ665 == 2 ~ 0,
      PAQ665 == 1 & !is.na(PAQ670) & !is.na(PAD675) ~ 4 * PAQ670 * PAD675,
      TRUE ~ NA_real_
    ),
    leisure_met_min_week = vigorous_met + moderate_met
  ) %>%
  select(SEQN, leisure_met_min_week, PAQ650, PAQ665)

demo <- read_xpt_url(urls$demo) %>%
  transmute(
    SEQN,
    age = as.numeric(RIDAGEYR),
    sex = factor(RIAGENDR),
    race_raw = as.numeric(RIDRETH3),
    education_raw = as.numeric(DMDEDUC2),
    WTMEC2YR = as.numeric(WTMEC2YR),
    SDMVSTRA = as.numeric(SDMVSTRA),
    SDMVPSU = as.numeric(SDMVPSU)
  )

bmx <- read_xpt_url(urls$bmx) %>%
  transmute(SEQN, bmi = as.numeric(BMXBMI))

prepare_dat <- function(pax_df, require_ses = FALSE) {
  dat <- demo %>%
    inner_join(paq, by = "SEQN") %>%
    inner_join(pax_df, by = "SEQN") %>%
    inner_join(bmx, by = "SEQN") %>%
    mutate(
      race4 = case_when(
        race_raw %in% c(1, 2) ~ "Hispanic",
        race_raw == 3 ~ "Non-Hispanic White",
        race_raw == 4 ~ "Non-Hispanic Black",
        race_raw %in% c(6, 7) ~ "Other",
        TRUE ~ NA_character_
      ),
      race4 = factor(
        race4,
        levels = c("Non-Hispanic White", "Non-Hispanic Black", "Hispanic", "Other")
      ),
      education3 = case_when(
        education_raw %in% c(1, 2) ~ "<High school",
        education_raw %in% c(3, 4) ~ "High school/some college",
        education_raw == 5 ~ "College graduate+",
        TRUE ~ NA_character_
      ),
      education3 = factor(
        education3,
        levels = c("<High school", "High school/some college", "College graduate+")
      )
    ) %>%
    filter(
      age >= 20,
      !is.na(leisure_met_min_week),
      !is.na(mean_mims_per_valid_min),
      !is.na(bmi),
      !is.na(sex),
      !is.na(WTMEC2YR),
      WTMEC2YR > 0
    )

  if (require_ses) {
    dat <- dat %>% filter(!is.na(race4), !is.na(education3))
  }

  dat %>%
    mutate(
      age_group = cut(
        age,
        breaks = c(20, 35, 50, 65, Inf),
        right = FALSE,
        labels = c("20-34", "35-49", "50-64", "65+")
      ),
      log_leisure = log1p(leisure_met_min_week),
      log_device = log1p(mean_mims_per_valid_min)
    )
}

make_design <- function(dat) {
  svydesign(
    ids = ~SDMVPSU,
    strata = ~SDMVSTRA,
    weights = ~WTMEC2YR,
    nest = TRUE,
    data = dat
  )
}

model_table <- function(model, design) {
  denom_df <- degf(design)
  sm <- summary(model, df.resid = denom_df)
  cm <- sm$coefficients
  crit <- qt(0.975, df = denom_df)

  data.frame(
    term = rownames(cm),
    estimate = cm[, 1],
    std.error = cm[, 2],
    statistic = cm[, 3],
    p.value = cm[, 4],
    conf.low = cm[, 1] - crit * cm[, 2],
    conf.high = cm[, 1] + crit * cm[, 2],
    df = denom_df,
    row.names = NULL,
    check.names = FALSE
  )
}

fit_primary <- function(dat) {
  design <- make_design(dat)
  model <- svyglm(
    log_device ~ log_leisure + age + sex + bmi,
    design = design
  )
  list(model = model, design = design, table = model_table(model, design))
}

options(survey.lonely.psu = "adjust")

pax_primary <- build_pax(valid_min_threshold = 1200, min_days = 4)
dat <- prepare_dat(pax_primary, require_ses = FALSE)
design <- make_design(dat)

primary <- svyglm(
  log_device ~ log_leisure + age + sex + bmi,
  design = design
)

interaction <- svyglm(
  log_device ~ log_leisure * age_group + sex + bmi,
  design = design
)

ses_dat <- prepare_dat(pax_primary, require_ses = TRUE)
ses_design <- make_design(ses_dat)
ses_model <- svyglm(
  log_device ~ log_leisure + age + sex + bmi + race4 + education3,
  design = ses_design
)

no_bmi_model <- svyglm(
  log_device ~ log_leisure + age + sex,
  design = design
)

write.csv(
  model_table(primary, design),
  file.path(out_dir, "primary_model.csv"),
  row.names = FALSE
)
write.csv(
  model_table(interaction, design),
  file.path(out_dir, "age_interaction_model.csv"),
  row.names = FALSE
)
write.csv(
  model_table(ses_model, ses_design),
  file.path(out_dir, "ses_sensitivity_model.csv"),
  row.names = FALSE
)
write.csv(
  model_table(no_bmi_model, design),
  file.path(out_dir, "no_bmi_sensitivity_model.csv"),
  row.names = FALSE
)

# Participant counts by number of qualifying days under the primary day rule.
valid_day_distribution <- pax_raw %>%
  filter(
    !is.na(PAXVMD),
    !is.na(PAXMTSD),
    PAXVMD >= 1200,
    PAXMTSD >= 0
  ) %>%
  count(SEQN, name = "qualifying_days") %>%
  count(qualifying_days, name = "participants") %>%
  arrange(qualifying_days)
write.csv(
  valid_day_distribution,
  file.path(out_dir, "valid_day_distribution.csv"),
  row.names = FALSE
)

# Threshold sensitivity for the focal log-leisure coefficient.
sensitivity_specs <- list(
  list(name = "primary_valid1200_days4", valid = 1200, days = 4, wear = NULL),
  list(name = "valid1000_days4", valid = 1000, days = 4, wear = NULL),
  list(name = "valid1200_days3", valid = 1200, days = 3, wear = NULL),
  list(name = "valid1200_days5", valid = 1200, days = 5, wear = NULL),
  list(name = "wear1200_days4", valid = 0, days = 4, wear = 1200)
)

sensitivity_rows <- lapply(sensitivity_specs, function(spec) {
  px <- build_pax(
    valid_min_threshold = spec$valid,
    min_days = spec$days,
    wear_min_threshold = spec$wear
  )
  dx <- prepare_dat(px, require_ses = FALSE)
  fit <- fit_primary(dx)
  focal <- fit$table %>% filter(term == "log_leisure")
  data.frame(
    specification = spec$name,
    n = nrow(dx),
    estimate = focal$estimate,
    std.error = focal$std.error,
    statistic = focal$statistic,
    p.value = focal$p.value,
    conf.low = focal$conf.low,
    conf.high = focal$conf.high,
    df = focal$df
  )
})
threshold_sensitivity <- bind_rows(sensitivity_rows)
write.csv(
  threshold_sensitivity,
  file.path(out_dir, "threshold_sensitivity.csv"),
  row.names = FALSE
)

join_counts <- data.frame(
  stage = c(
    "demo_total",
    "demo_age20plus",
    "paq_total",
    "pax_primary_participants",
    "bmx_total",
    "primary_analytic",
    "ses_sensitivity_analytic"
  ),
  n = c(
    nrow(demo),
    sum(demo$age >= 20, na.rm = TRUE),
    nrow(paq),
    nrow(pax_primary),
    nrow(bmx),
    nrow(dat),
    nrow(ses_dat)
  )
)
write.csv(join_counts, file.path(out_dir, "qa_counts.csv"), row.names = FALSE)

primary_table <- model_table(primary, design)
focal <- primary_table %>% filter(term == "log_leisure")

summary_out <- list(
  design = "NHANES 2013-2014 cross-sectional complex survey",
  population = "Adults age 20+",
  n = nrow(dat),
  survey_design_df = degf(design),
  valid_day_rule = "PAXVMD >= 1200 valid minutes; >= 4 qualifying days",
  valid_day_rule_status = "analyst-defined completeness rule, not a CDC standard",
  device_metric = "mean daily PAXMTSD / PAXVMD (MIMS per valid minute)",
  self_report_metric = "leisure MET-min/week from GPAQ recreational items",
  survey_weight = "WTMEC2YR",
  strata = "SDMVSTRA",
  psu = "SDMVPSU",
  primary_formula = "log1p(device movement density) ~ log1p(leisure MET-min/week) + age + sex + BMI",
  primary_log_leisure = list(
    estimate = focal$estimate,
    std_error = focal$std.error,
    statistic = focal$statistic,
    p_value = focal$p.value,
    conf_low = focal$conf.low,
    conf_high = focal$conf.high,
    df = focal$df
  ),
  unweighted_descriptives = list(
    leisure_met_min_week_median = median(dat$leisure_met_min_week, na.rm = TRUE),
    leisure_met_min_week_q25 = unname(quantile(dat$leisure_met_min_week, 0.25, na.rm = TRUE)),
    leisure_met_min_week_q75 = unname(quantile(dat$leisure_met_min_week, 0.75, na.rm = TRUE)),
    movement_density_median = median(dat$mean_mims_per_valid_min, na.rm = TRUE),
    valid_days_median = median(dat$valid_days, na.rm = TRUE)
  )
)

write_json(
  summary_out,
  file.path(out_dir, "summary.json"),
  pretty = TRUE,
  auto_unbox = TRUE
)
print(summary_out)
