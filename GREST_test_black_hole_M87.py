import math

def calculate_grest(g_newton):
    a0 = 1.129e-10 
    return math.sqrt(g_newton**2 + (g_newton * a0))

# M87* Event Horizon Data
g_newton_bh = 6.0e10 
g_observed = calculate_grest(g_newton_bh)
boost = g_observed / g_newton_bh

print(f"Test Result for Black Hole (M87*):")
print(f"Boost Factor: {round(boost, 10)}x")