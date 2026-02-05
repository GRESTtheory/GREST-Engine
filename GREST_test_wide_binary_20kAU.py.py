import math

# The Engine Logic
def calculate_grest(g_newton):
    a0 = 1.129e-10 
    return math.sqrt(g_newton**2 + (g_newton * a0))

# Benchmark: Wide Binary at 20,000 AU
g_newton_wb = 2.36e-11 
g_observed = calculate_grest(g_newton_wb)

# Calculate the "Boost Factor" (g_obs / g_newton)
boost = g_observed / g_newton_wb

print(f"Newtonian Gravity: {g_newton_wb}")
print(f"GREST Observed Gravity: {g_observed}")
print(f"Boost Factor: {round(boost, 2)}x")