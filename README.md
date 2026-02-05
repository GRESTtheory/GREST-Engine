# GREST v1.1: Universal Metric Response Validation Package

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18489321.svg)](https://doi.org/10.5281/zenodo.18489321)

## Overview
Official validation suite for the **GREST (Quadratic Metric Response)** model. GREST provides a unified explanation for gravitational anomalies across six distinct physical scales without the requirement for Dark Matter.

## Unit-Locked Constants (v1.1)
- **H0**: 73.0 km/s/Mpc
- **a0**: 1.129e-10 m/s² (Calculated as $c \cdot H_0 / 2\pi$)

## Governing Formula
Observed acceleration ($g_{obs}$) is derived from Newtonian acceleration ($g_N$):
$$g_{obs} = \sqrt{g_N^2 + g_N a_0}$$

## Validation Results
| System | Newtonian $g_N$ | GREST $g_{obs}$ | Boost Factor |
| :--- | :--- | :--- | :--- |
| **Wide Binaries** | 2.36e-11 | 5.68e-11 | **2.4x** |
| **NGC 6503** | 2.80e-11 | 6.28e-11 | **2.24x** |
| **Coma Cluster** | 1.05e-11 | 3.60e-11 | **3.43x** |

## Files
- `GREST_engine.py`: Core acceleration law implementation.
- `GREST_run_all_tests.py`: Master script to replicate all results.
- `GREST_v1_1_Universal_Validation...pdf`: Formal theoretical derivation.

## Citation
Gresty, J. (2026). GREST v1.1: Universal Metric Response Validation Package. Zenodo. https://doi.org/10.5281/zenodo.18489321
