
def speed():
    distance = float(input("Enter distance (in meters): "))
    time = float(input("Enter time (in seconds): "))

    if time == 0:
        print("Time cannot be zero!")
    else:
        speed = distance / time
        print(f"The speed is {speed} m/s")


def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))

    force = mass * acceleration
    print(f"The force is {force} N")


def density():
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m^3): "))

    if volume == 0:
        print("Volume cannot be zero!")
    else:
        density = mass / volume
        print(f"The density is {density} kg/m^3")


def weight():
    mass = float(input("\nEnter mass (kg): "))
    gravity = 9.8

    weight = mass * gravity
    print(f"The weight is {weight} N")


def work_done():
    force = float(input("\nEnter force (N): "))
    distance = float(input("Enter distance (m): "))

    work = force * distance
    print(f"Work Done is {work} J")


while True:
    print("\nPHYSICS CALCULATOR")

    formulae = [
        "1. Speed",
        "2. Force",
        "3. Density",
        "4. Weight",
        "5. Work Done"
    ]

    for form in formulae:
        print(form)

    entry = input("Enter a quantity: ")

    if entry == "1":
        speed()

    elif entry == "2":
        force()

    elif entry == "3":
        density()

    elif entry == "4":
        weight()

    elif entry == "5":
        work_done()

    else:
        print("Input a valid quantity")

    again = input(
        "Do you want to calculate something else? (yes or no): "
    )

    if again.lower() == "yes":
        continue
    else:
        print("Thank you for using the Physics Calculator!")
        break
