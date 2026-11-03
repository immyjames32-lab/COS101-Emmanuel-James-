# 1. Speed = Distance / Time
distance = float(input("Enter distance (m): "))
time = float(input("Enter time (s): "))
speed = distance / time
print("Speed =", speed, "m/s")

# 2. Force = Mass × Acceleration
mass = float(input("\nEnter mass (kg): "))
acceleration = float(input("Enter acceleration (m/s²): "))
force = mass * acceleration
print("Force =", force, "N")

# 3. Density = Mass / Volume
mass = float(input("\nEnter mass (kg): "))
volume = float(input("Enter volume (m³): "))
density = mass / volume
print("Density =", density, "kg/m³")

# 4. Weight = Mass × Gravity
mass = float(input("\nEnter mass (kg): "))
gravity = 9.8
weight = mass * gravity
print("Weight =", weight, "N")

# 5. Work Done = Force × Distance
force = float(input("\nEnter force (N): "))
distance = float(input("Enter distance (m): "))
work = force * distance
print("Work Done =", work, "J")
