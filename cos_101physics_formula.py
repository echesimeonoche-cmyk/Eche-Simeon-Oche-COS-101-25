def show_menu():
    print("\nWelcome to the Physics Calculator")
    print("\nSelect a Physics Formular:")
    print("1. Speed = Distance/time")
    print("2. Momentum = Mass * Velocity")
    print("3. Work done = Force * Distance")
    print("4. Pressure = Force/Area")
    print("5. Density = Mass/Volume")


def calculate(choice):
    if choice == "1":
        # Speed = Distance / Time
        d = float(input("Enter Distance (m): "))
        t = float(input("Enter Time (s): "))
        print(f"speed = {d / t} m/s")

    elif choice == "2":
        # Momentum = Mass * Velocity
        m = float(input("Enter Mass (kg): "))
        v = float(input("Enter Velocity (m/s): "))
        print(f"momentum = {m * v}  kgms")

    elif choice == "3":
        # Work_done = Force * Distance
        f = float(input("Enter Force (N): "))
        d = float(input("Enter Distance (m): "))
        print(f"work done = {f * d} Nm")

    elif choice == "4":
        # Pressure = Force/Area
        f = float(input("Enter Force (N): "))
        a = float(input("Enter Area (m^2): "))
        print(f"Pressure = {f / a} Nm^2")

    elif choice == "5":
        # Density = Mass/Volume
        m = float(input("Enter Mass (kg): "))
        v = float(input("Enter Volume (m^3): "))
        print(f"Density = {m / v} kgm^3")

    else:
        print("Please enter a valid choice")

def main():
    while True:
        show_menu()
        choice = input("Please enter your choice(1-5) or 'q' to quit: ")

        if choice.lower() == "q":
            print("Thank you for using Physics Calculator")

            calculate(choice)

if __name__ == "__main__":
    main()



