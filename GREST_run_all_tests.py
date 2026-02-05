import math

def calculate_grest(g_newton):
    a0 = 1.129e-10 
    return math.sqrt(g_newton**2 + (g_newton * a0))

# Test Data: [System Name, Newtonian gN]
tests = [
    ["Black Hole (M87*)", 6.0e10],
    ["The Sun (1 AU)", 0.00593],
    ["Wide Binary (20kAU)", 2.36e-11],
    ["Galaxy (NGC 6503)", 2.80e-11],
    ["Galaxy (DF2)", 4.20e-11],
    ["Cluster (Coma)", 1.05e-11]
]

print(f"{'SYSTEM':<20} | {'gN (Newton)':<12} | {'g_obs (GREST)':<12} | {'BOOST'}")
print("-" * 65)

for name, gn in tests:
    g_obs = calculate_grest(gn)
    boost = g_obs / gn
    print(f"{name:<20} | {gn:<12.2e} | {g_obs:<12.2e} | {round(boost, 2)}x")