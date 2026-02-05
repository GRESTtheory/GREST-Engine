import math

def calculate_grest(g_newton):
    a0 = 1.129e-10 
    return math.sqrt(g_newton**2 + (g_newton * a0))

# Solar System Data at 1 AU (Earth's Orbit)
g_newton_sun = 0.00593
g_observed = calculate_grest(g_newton_sun)
boost = g_observed / g_newton_sun

print(f"Test Result for The Sun (1 AU):")
print(f"Boost Factor: {round(boost, 10)}x")