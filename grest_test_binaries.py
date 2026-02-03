import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# TEST 3: WIDE BINARY STARS (Micro-Gravity)
# ==========================================

H0_km_s_Mpc = 73.0
c = 2.99792e8
H0_per_sec = H0_km_s_Mpc * 3.24078e-20 
A0_GLOBAL = (c * H0_per_sec) / (2 * np.pi)

# Gaia Data (Chae et al. 2023)
s_kau = np.array([0.5, 1.0, 2.0, 5.0, 10.0, 20.0])
boost_obs = np.array([1.0, 1.02, 1.08, 1.25, 1.38, 1.45])

# GREST Calculation
M_total = 2.0 * 1.989e30 
r_meters = s_kau * 1000 * 1.496e11
g_newton = (6.674e-11 * M_total) / (r_meters**2)
g_obs = np.sqrt(g_newton**2 + g_newton * A0_GLOBAL)
boost_pred = g_obs / g_newton

# Plot
plt.figure(figsize=(9, 6))
plt.axhline(y=1.0, color='k', linestyle='--', label='Newton')
plt.plot(s_kau, boost_obs, 'ko', label='Gaia Data')
plt.plot(s_kau, boost_pred, 'r-', linewidth=3, label='GREST Prediction')
plt.title("Wide Binary Gravity Boost")
plt.xlabel("Separation (kAU)")
plt.ylabel("Boost Factor")
plt.legend()
plt.savefig("grest_wide_binary_test.png")
plt.show()