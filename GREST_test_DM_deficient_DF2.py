import math

def calculate_grest(g_newton):
    a0 = 1.129e-10 
    return math.sqrt(g_newton**2 + (g_newton * a0))

# NGC 1052-DF2 Data (The "No Dark Matter" Galaxy)
g_newton_df2 = 4.2e-11
g_observed = calculate_grest(g_newton_df2)
boost = g_observed / g_newton_df2

print(f"Test Result for DM-Deficient Galaxy (DF2):")
print(f"Boost Factor: {round(boost, 2)}x")