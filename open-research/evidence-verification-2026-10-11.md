# Research Evidence and Version Verification — 11 October 2026

This public summary distinguishes checks actually performed from work not yet independently reproduced. It contains no private correspondence or unpublished coursework.

## Research identity and systematic reviews

- Catherine reports **two systematic evidence-synthesis projects in progress**. Exact titles, authorship, protocol records, review stages and identifiers have not yet been independently verified. One OSF DOI has been reported, but the exact DOI has not been recovered or uniquely resolved; **no OSF URL is asserted**.
- No ORCID iD has been uniquely verified as belonging to Catherine Ge; **no ORCID URL is asserted**.
- An unverified identifier must not be represented as a publication or registered protocol.

## Secondary analyses — repository/output consistency check

| Analysis | Existing reported result checked against saved results, validation and website | Current verification level |
| --- | --- | --- |
| HINTS 7 (2024) | Adjusted OR 1.83 (95% CI 1.42–2.34); complete-case n=5,183; JK1 50 replicates. README historical status was reconciled to its 2 October 2026 validation report. | Desk audit; earlier script execution described in project validation report |
| HINTS 6 + 7 (2022/2024) | Survey-cycle interaction OR 1.20 (95% CI 0.83–1.73), p=0.330, pooled n=10,838; 100 Rizzo replicates. Saved coefficient beta 0.1820247 and SE 0.1858702 imply exp(beta)=1.19965 (rounds to 1.20). | Desk audit and independent arithmetic check of saved coefficient; not raw-data replication |
| NHANES 2013–14 PAM | Adjusted beta 0.00876 (95% CI 0.00347–0.01404), p=0.0030, n=4,726; saved beta 0.008756585 and SE 0.002480304. | Desk audit and coefficient/SE agreement; not raw-data replication |

These are secondary, cross-sectional or repeated cross-sectional studies. Associations do not establish causality. HINTS outcomes are self-reported health-information use; NHANES MIMS is not MVPA time. These are independent research-development artifacts, **not peer-reviewed journal publications**.

**Reproducibility remaining:** a fresh independent download/execution of official survey data using pinned versions, checksumed inputs, script revision, runtime environment and dated output comparisons. As of this report, that step **has not been performed**.

## Physical Activity Adherence — Digital Intervention Micro Map

- **v0.1 frozen:** PA001–PA010; ten unique study IDs in the `micro_map_manifest.csv` on the checked default branch. Jointly maintained by Catherine Ge and Starr Choi. `CITATION.cff` lists Zenodo DOI [10.5281/zenodo.23178043](https://doi.org/10.5281/zenodo.23178043), CC BY 4.0, and `date-released: 2026-10-06`. The original `VERSION` file separately records `release_date=2026-10-05`. This is an archival metadata discrepancy **documented here, without altering the frozen release**; publication date should be independently read from Zenodo for definitive citation.
- **v0.2 working:** PA001–PA015; fifteen unique IDs checked in `v0.2/micro_map_manifest_v0.2.csv`. It adds phase, active comparator, adaptation, exposure/engagement and maintenance fields. Its README identifies v0.2 as not frozen or deposited.
- A CSV parse of both manifests confirms that all **10 original rows × 10 original fields (100 corresponding cells)** are exactly preserved in v0.2; the first 10 column names match, v0.2 adds five columns and five new rows, and the IDs are unique in each version. This source-data equality check is **not** an independent source-paper verification of the research coding.
- [Frozen v0.1 page](./physical-activity-adherence-map/releases/v0.1/) · [Working v0.2 page](./physical-activity-adherence-map/v0.2/) · [v0.1 CSV](./physical-activity-adherence-map/micro_map_manifest.csv) · [v0.2 CSV](./physical-activity-adherence-map/v0.2/micro_map_manifest_v0.2.csv)

## Formal research training

Catherine is taking **PU5027 Fundamentals of Research Design (Online)** at the University of Aberdeen in the 2026–27 academic year. Status: **in progress**, not a completed module, degree, graded assessment, transcript or reference. No submitted work or assessed feedback was independently verified in this check.

## Research exchange and publication boundary

Targeted contact drafts, academic-review records and correspondence logs are maintained privately pending Catherine's review. No public Research Note is represented here as Catherine-approved solely because a draft or GitHub discussion exists. No email, reply or supervisory relationship is claimed without dated evidence.

*Desk audit and public evidence check, 11 October 2026; scope and limitations stated explicitly.*
