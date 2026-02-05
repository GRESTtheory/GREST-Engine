# GREST v1.1: Universal Metric Response Validation Package

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18489321.svg)](https://doi.org/10.5281/zenodo.18489321)

## Overview
This repository contains the mathematical engine and verification suite for the **Quadratic Metric Response (GREST)** model. GREST provides a unified explanation for gravitational anomalies across six distinct physical scales without requiring Dark Matter.

## Citation
If you use this model or the validation data, please cite the official archive:
> Gresty, J. (2026). GREST v1.1: Universal Metric Response Validation Package. Zenodo. https://doi.org/10.5281/zenodo.18489321

## Scale Benchmarks
Validation is successful when the GREST engine matches the following observed boosts:

| System | Newtonian $g_N$ ($m/s^2$) | GREST $g_{obs}$ ($m/s^2$) | Boost |
| :--- | :--- | :--- | :--- |
| Black Hole (M87*) | 6.00e+10 | 6.00e+10 | **1.0x** |
| The Sun (1 AU) | 5.93e-03 | 5.93e-03 | **1.0x** |
| Wide Binary (20kAU) | 2.36e-11 | 5.68e-11 | **2.4x** |
| Galaxy (NGC 6503) | 2.80e-11 | 6.28e-11 | **2.24x** |
| Galaxy (DF2) | 4.20e-11 | 8.07e-11 | **1.92x** |
| Cluster (Coma) | 1.05e-11 | 3.60e-11 | **3.43x** |

## Execution
To verify all benchmarks locally, ensure you have Python installed and run:
```bash
python GREST_run_all_tests.py