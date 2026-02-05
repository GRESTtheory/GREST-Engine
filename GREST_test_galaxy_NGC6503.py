import math

def calculate_grest(g_newton):
    a0 = 1.129e-10 
    return math.sqrt(g_newton**2 + (g_newton * a0))

# NGC 6503 Data (Outer Edge / SPARC)
g_newton_gal = 2.80e-11
g_observed = calculate_grest(g_newton_gal)
boost = g_observed / g_newton_gal

print(f"Test Result for Galaxy NGC 6503 (Outer Edge):")
print(f"Boost Factor: {round(boost, 2)}x")