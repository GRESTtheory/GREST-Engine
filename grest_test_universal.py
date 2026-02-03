import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# TEST 2: UNIVERSALITY (Small vs Giant Galaxy)
# ==========================================

H0_km_s_Mpc = 73.0
c = 2.99792e8
H0_per_sec = H0_km_s_Mpc * 3.24078e-20 
A0_GLOBAL = (c * H0_per_sec) / (2 * np.pi)

def grest_prediction(v_baryon_kms, r_kpc):
    r_m = r_kpc * 3.0857e19
    v_bar_ms = v_baryon_kms * 1000.0
    g_newton = (v_bar_ms**2) / r_m
    g_obs = np.sqrt(g_newton**2 + g_newton * A0_GLOBAL)
    v_obs_ms = np.sqrt(g_obs * r_m)
    return v_obs_ms / 1000.0

# Data Loading
r_A = np.array([1.25, 2.50, 3.76, 5.01, 6.26, 7.51, 8.77, 10.02, 12.52, 15.03, 17.54, 20.04, 22.55])
v_bar_A = np.array([85.1, 105.2, 107.8, 105.2, 100.8, 96.0, 91.3, 87.0, 79.5, 73.1, 67.8, 63.3, 59.5])
v_obs_A = np.array([92.1, 113.1, 118.2, 120.2, 119.8, 119.0, 118.4, 118.5, 119.9, 120.0, 118.7, 116.7, 115.0])

r_B = np.array([ 2.0,  4.0,  6.0,  8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0])
v_bar_B = np.array([130.0, 175.0, 185.0, 180.0, 170.0, 160.0, 150.0, 140.0, 130.0, 122.0, 115.0, 108.0])
v_obs_B = np.array([145.0, 210.0, 235.0, 242.0, 245.0, 247.0, 245.0, 242.0, 240.0, 238.0, 235.0, 232.0])

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot A (Dwarf)
ax1.plot(r_A, v_obs_A, 'ko', label='Data')
ax1.plot(r_A, grest_prediction(v_bar_A, r_A), 'r-', linewidth=3, label='GREST')
ax1.set_title("Small Galaxy (NGC 6503)")
ax1.legend()

# Plot B (Giant)
ax2.plot(r_B, v_obs_B, 'ko', label='Data')
ax2.plot(r_B, grest_prediction(v_bar_B, r_B), 'r-', linewidth=3, label='GREST')
ax2.set_title("Giant Galaxy (NGC 7331)")
ax2.legend()

plt.savefig("grest_universal_proof.png")
plt.show()