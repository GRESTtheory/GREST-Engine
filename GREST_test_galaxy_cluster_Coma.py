import math

def calculate_grest(g_newton):
    # Acceleration floor locked to H0 = 73.0 
    a0 = 1.129e-10 
    
    # Quadratic Metric Response Law 
    g_observed = math.sqrt(g_newton**2 + (g_newton * a0))
    
    return g_observed

# Coma Cluster Data (Massive Scale)
# Newtonian gravity is extremely low at cluster outskirts
g_newton_coma = 1.05e-11
g_observed = calculate_grest(g_newton_coma)
boost = g_observed / g_newton_coma

print(f"Test Result for Coma Cluster (Outskirts):")
print(f"Boost Factor: {round(boost, 2)}x")