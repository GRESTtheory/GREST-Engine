Title: Universal Validation of the Metric Response of Space-Time (GREST v1.1)Description:This package provides the Python engine and validation scripts for the GREST v1.1 gravitational model. This model replaces the Dark Matter hypothesis with a single acceleration law locked to the Hubble Constant ($H_0 = 73.0$).The GREST Law:$g_{obs} = \sqrt{g_N^2 + g_N a_0}$The Universal Constant:$a_0 = 1.129 \times 10^{-10} \text{ m/s}^2$Instructions:Ensure Python 3.x is installed.Keep GREST_engine.py in the same directory as the test scripts.Run any of the GREST_test_...py files to see the validation results.Contents:GREST_v1_1_Validation.pdf (Manuscript)GREST_engine.py (Master Logic)GREST_test_black_hole_M87.pyGREST_test_the_sun_1AU.pyGREST_test_wide_binary_20kAU.pyGREST_test_galaxy_NGC6503.pyGREST_test_DM_deficient_DF2.pyGREST_test_galaxy_cluster_Coma.py

GREST v1.1 VALIDATION PACKAGE
-----------------------------
This package contains the theoretical manuscript, core engine, and 
automated verification scripts for the GREST model.

FILE INVENTORY:
1.  GREST_v1_1_Universal_Validation.pdf - Primary Manuscript
2.  GREST_engine.py                     - Core Logic
3.  GREST_run_all_tests.py              - Master Verification Script
4.  validation_results.txt              - Benchmark Reference Sheet
5.  GREST_test_black_hole_M87.py        - Relativistic Test
6.  GREST_test_the_sun_1AU.py           - Solar System Test
7.  GREST_test_wide_binary_20kAU.py     - Stellar Test
8.  GREST_test_galaxy_NGC6503.py        - Galactic Test
9.  GREST_test_DM_deficient_DF2.py      - Low-DM Test
10. GREST_test_galaxy_cluster_Coma.py   - Cluster Test

INSTRUCTIONS:
Run 'GREST_run_all_tests.py' to verify the model across all scales.