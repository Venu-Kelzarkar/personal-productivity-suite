def start_converter():
    while True:
        print("\nUNIT CONVERTER")
        print("1. KM → Miles")
        print("2. KG → Pounds")
        print("3. Celsius → Fahrenheit")
        print("4. Back")

        ch = input("Choice: ")

        if ch == "1":
            print("Miles:", float(input("KM: ")) * 0.621371)

        elif ch == "2":
            print("Pounds:", float(input("KG: ")) * 2.20462)

        elif ch == "3":
            c = float(input("Celsius: "))
            print("Fahrenheit:", (c * 9/5) + 32)

        elif ch == "4":
            break