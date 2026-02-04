# GREST-Engine Validation (v1.0)

This repository is the official source of truth for the **GREST Effective Field Law** (v1.0). It contains the master validation script and data used to predict gravitational dynamics across galactic and stellar scales without the use of dark matter parameters.

## Unit-Locked Constants
To ensure reproducibility, all tests use the following fixed values:
* **H0**: 73.0 km/s/Mpc
* **c**: 299,792,458 m/s
* **a0**: 1.129e-10 m/s^2 (Calculated as (c * H0) / 2π)

## Governing Formula
Observed acceleration ($g_{obs}$) is derived from Newtonian acceleration ($g_N$):
$$g_{obs} = \sqrt{g_N^2 + g_N a_0}$$

## Validation Results

### Internal (Galactic)
| System | Observed | GREST Predicted | Accuracy |
| :--- | :--- | :--- | :--- |
| NGC 6503 | 133.0 km/s | 133.28 km/s | 99.79% |
| NGC 1052-DF2 | 7.9 km/s | 7.40 km/s | 93.66% |
| NGC 7331 | 205.0 km/s | 203.81 km/s | 99.42% |

### External (Stellar)
* **Gaia Wide Binaries**: Predicts a **2.19x** gravity boost at 20 kAU, aligning with reported anomalous excess velocities.

## Files
* `grest_engine_v1.py`: The master validation script.
* `GREST_Validation_Final.csv`: Detailed validation data.
* `references.bib`: BibTeX entries for data sources.

---
**DOI**: [Pending Zenodo Submission]
