import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# TEST 1: SINGLE GALAXY VALIDATION (NGC 6503)
# ==========================================

H0_km_s_Mpc = 73.0
c = 2.99792e8
H0_per_sec = H0_km_s_Mpc * 3.24078e-20 
A0_GLOBAL = (c * H0_per_sec) / (2 * np.pi)

# NGC 6503 Data (The Dwarf)
r_data = np.array([1.25, 2.50, 3.76, 5.01, 6.26, 7.51, 8.77, 10.02, 12.52, 15.03, 17.54, 20.04, 22.55])
v_obs = np.array([92.1, 113.1, 118.2, 120.2, 119.8, 119.0, 118.4, 118.5, 119.9, 120.0, 118.7, 116.7, 115.0])
v_newton = np.array([85.1, 105.2, 107.8, 105.2, 100.8, 96.0, 91.3, 87.0, 79.5, 73.1, 67.8, 63.3, 59.5])

# GREST Prediction
r_m = r_data * 3.0857e19
v_ms = v_newton * 1000.0
g_newton = (v_ms**2) / r_m
g_obs = np.sqrt(g_newton**2 + g_newton * A0_GLOBAL)
v_pred = np.sqrt(g_obs * r_m) / 1000.0

# Plot
plt.figure(figsize=(10, 7))
plt.plot(r_data, v_newton, 'k--', label='Standard Gravity (Fails)')
plt.errorbar(r_data, v_obs, yerr=2.0, fmt='ko', label='Real Data (NGC 6503)')
plt.plot(r_data, v_pred, 'r-', linewidth=3, label='GREST Prediction')
plt.title("Test 1: NGC 6503 Validation")
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (km/s)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("grest_real_data_test.png") # Creates the Proof Image
plt.show()