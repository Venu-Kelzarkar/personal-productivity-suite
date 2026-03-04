import math

def start_calculator():
    while True:
        print("\nCALCULATOR")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Power")
        print("7. Back")

        choice = input("Enter choice: ")

        if choice == "7":
            break

        if choice == "5":
            num = float(input("Enter number: "))
            print("Result:", math.sqrt(num))
            continue

        if choice == "6":
            base = float(input("Enter base: "))
            exp = float(input("Enter exponent: "))
            print("Result:", math.pow(base, exp))
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            print("Result:", "Cannot divide by zero" if b == 0 else a / b)
        else:
            print("Invalid choice!")