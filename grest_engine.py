import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# GREST-Engine: Theoretical Validator
# Implements equations 1-4 from Gresty (2026)
# ==========================================

# --- 1. PHYSICAL CONSTANTS ---
# Hubble Parameter H0 = 73 km/s/Mpc
# Conversion factor: 1 Mpc = 3.086e19 km
# H0 in SI units (1/s)
H0_km_s_Mpc = 73.0
H0_per_sec = H0_km_s_Mpc * 3.24078e-20 

c = 2.99792e8  # Speed of light (m/s)
G = 6.67430e-11 # Gravitational Constant

# --- 2. THEORETICAL CORE ---

def calculate_a0():
    """
    Implements Equation 1: The Global Acceleration Floor
    a0 = (c * H0) / 2pi
    """
    return (c * H0_per_sec) / (2 * np.pi)

# Calculate the global constant once
A0_GLOBAL = calculate_a0()

def grest_metric_response(g_newton, density_contrast=0.1, gamma=1):
    """
    Implements Equation 2 & 3: The Effective Field Law
    
    Parameters:
    -----------
    g_newton : float or array
        The standard Newtonian acceleration (GM/r^2)
    density_contrast (delta) : float
        Local environmental density. If delta > 3, theory saturates to Newton.
    gamma : int
        Morphology parameter. 1 for Disks (Rotation), 0 for Spheres (Pressure).
    """
    
    # Saturation Ansatz (Equation 4)
    # Recover Newtonian behavior in high-density environments (delta > 3)
    saturation_S = np.maximum(0, 1 - (density_contrast / 3.0))
    
    # Local effective acceleration floor (Equation 3)
    a0_local = A0_GLOBAL * saturation_S * gamma
    
    # Quadratic Composition (Equation 2)
    # g_obs = sqrt( g_N^2 + g_N * a0_local )
    g_obs = np.sqrt(g_newton**2 + g_newton * a0_local)
    
    return g_obs

# --- 3. DEMONSTRATION (TOY MODEL) ---

def run_validation_plot():
    print(f"[-] GREST Global Acceleration Scale (a0): {A0_GLOBAL:.3e} m/s^2")
    
    # Define a grid of radii (0.1 kpc to 30 kpc)
    kpc_to_m = 3.0857e19
    r_kpc = np.linspace(0.1, 30, 200)
    r_m = r_kpc * kpc_to_m
    
    # Define a simple Baryonic Mass Profile (Freeman Disk approximation)
    # Mass grows with radius, then flattens at M_total
    M_solar = 1.989e30
    M_total = 5.0e10 * M_solar
    
    # Cumulative mass enclosed at radius r
    mass_enclosed = M_total * (1 - np.exp(-r_kpc / 3.0)) 
    
    # A. Calculate Standard Newtonian Gravity (g_N)
    g_newton = (G * mass_enclosed) / (r_m**2)
    v_newton = np.sqrt(g_newton * r_m) / 1000.0  # Convert to km/s
    
    # B. Calculate GREST Gravity (g_obs)
    # Using typical disk density contrast (delta < 3) and gamma=1
    g_grest = grest_metric_response(g_newton, density_contrast=0.1, gamma=1)
    v_grest = np.sqrt(g_grest * r_m) / 1000.0    # Convert to km/s
    
    # C. Plotting
    plt.figure(figsize=(10, 6))
    
    # Plot Newtonian (Expected to fall)
    plt.plot(r_kpc, v_newton, 'k--', linewidth=1.5, label='Newtonian (Baryons Only)')
    
    # Plot GREST (Expected to stay flat)
    plt.plot(r_kpc, v_grest, 'b-', linewidth=2.5, label='GREST Prediction (Eq. 2)')
    
    # Styling
    plt.title(f"GREST Validation: Rotation Curve Flatness\nDerived $a_0$ = {A0_GLOBAL:.2e} $m/s^2$ (from $H_0$={H0_km_s_Mpc})")
    plt.xlabel("Galactic Radius (kpc)")
    plt.ylabel("Rotational Velocity (km/s)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save output
    output_filename = "grest_validation_curve.png"
    plt.savefig(output_filename, dpi=300)
    print(f"[-] Validation plot saved to {output_filename}")
    plt.show()

if __name__ == "__main__":
    run_validation_plot()