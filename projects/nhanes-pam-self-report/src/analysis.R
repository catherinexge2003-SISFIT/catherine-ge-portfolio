#!/usr/bin/env Rscript

# NHANES 2013-2014: device-measured movement vs self-reported leisure PA

suppressPackageStartupMessages({
  library(haven)
  library(dplyr)
  library(tidyr)
  library(survey)
  library(broom)
  library(jsonlite)
})

base <- "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2013/DataFiles"
urls <- list(
  paxday = paste0(base, "/PAXDAY_H.xpt"),
  paq = paste0(base, "/PAQ_H.xpt"),
  demo = paste0(base, "/DEMO_H.xpt"),
  bmx = paste0(base, "/BMX_H.xpt")
)

out_dir <- file.path(dirname(dirname(normalizePath(sys.frame(1)$ofile %||% "src/analysis.R"))), "results")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

read_xpt_url <- function(url) {
  tf <- tempfile(fileext = ".xpt")
  download.file(url, tf, mode = "wb", quiet = TRUE)
  on.exit(unlink(tf), add = TRUE)
  read_xpt(tf)
}

clean_minutes <- function(x) {
  x <- as.numeric(x)
  x[x %in% c(7777, 9999, 77, 99)] <- NA_real_
  x
}

pax <- read_xpt_url(urls$paxday) %>%
  transmute(
    SEQN,
    PAXDAYD = as.numeric(PAXDAYD),
    PAXVMD = as.numeric(PAXVMD),
    PAXMTSD = as.numeric(PAXMTSD)
  ) %>%
  filter(!is.na(PAXVMD), !is.na(PAXMTSD), PAXVMD >= 1200) %>%
  mutate(mims_per_valid_min = PAXMTSD / PAXVMD) %>%
  group_by(SEQN) %>%
  summarise(
    valid_days = n(),
    mean_mims_per_valid_min = mean(mims_per_valid_min, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  filter(valid_days >= 4)

paq <- read_xpt_url(urls$paq) %>%
  mutate(
    across(c(PAQ650, PAQ655, PAD660, PAQ665, PAQ670, PAD675), as.numeric),
    PAQ655 = clean_minutes(PAQ655),
    PAD660 = clean_minutes(PAD660),
    PAQ670 = clean_minutes(PAQ670),
    PAD675 = clean_minutes(PAD675),
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
  select(SEQN, leisure_met_min_week)

demo <- read_xpt_url(urls$demo) %>%
  transmute(
    SEQN,
    age = as.numeric(RIDAGEYR),
    sex = factor(RIAGENDR),
    race = factor(RIDRETH3),
    education = factor(DMDEDUC2),
    WTMEC2YR = as.numeric(WTMEC2YR),
    SDMVSTRA = as.numeric(SDMVSTRA),
    SDMVPSU = as.numeric(SDMVPSU)
  )

bmx <- read_xpt_url(urls$bmx) %>%
  transmute(SEQN, bmi = as.numeric(BMXBMI))

dat <- demo %>%
  inner_join(paq, by = "SEQN") %>%
  inner_join(pax, by = "SEQN") %>%
  inner_join(bmx, by = "SEQN") %>%
  filter(
    age >= 18,
    !is.na(leisure_met_min_week),
    !is.na(mean_mims_per_valid_min),
    !is.na(bmi),
    !is.na(WTMEC2YR),
    WTMEC2YR > 0
  ) %>%
  mutate(
    age_group = cut(
      age,
      breaks = c(18, 35, 50, 65, Inf),
      right = FALSE,
      labels = c("18-34", "35-49", "50-64", "65+")
    ),
    log_leisure = log1p(leisure_met_min_week),
    log_device = log1p(mean_mims_per_valid_min)
  )

options(survey.lonely.psu = "adjust")
design <- svydesign(
  ids = ~SDMVPSU,
  strata = ~SDMVSTRA,
  weights = ~WTMEC2YR,
  nest = TRUE,
  data = dat
)

primary <- svyglm(
  log_device ~ log_leisure + age_group + sex + race + education + bmi,
  design = design
)

interaction <- svyglm(
  log_device ~ log_leisure * age_group + sex + race + education + bmi,
  design = design
)

write.csv(tidy(primary, conf.int = TRUE), file.path(out_dir, "primary_model.csv"), row.names = FALSE)
write.csv(tidy(interaction, conf.int = TRUE), file.path(out_dir, "age_interaction_model.csv"), row.names = FALSE)

summary <- list(
  design = "NHANES 2013-2014 cross-sectional complex survey",
  n = nrow(dat),
  valid_day_rule = "PAXVMD >= 1200 minutes; >= 4 days",
  device_metric = "mean PAXMTSD / PAXVMD",
  self_report_metric = "leisure MET-min/week from GPAQ items",
  survey_weight = "WTMEC2YR",
  strata = "SDMVSTRA",
  psu = "SDMVPSU"
)
write_json(summary, file.path(out_dir, "summary.json"), pretty = TRUE, auto_unbox = TRUE)
print(summary)
