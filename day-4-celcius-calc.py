def celcius2fahrenheit(celcius: float) -> float:
    fahrenheit = celcius * (9 / 5) + 32
    return fahrenheit


def fahrenheit2celcius(fahrenheit: float) -> float:
    celcius = (fahrenheit - 32) * 5 / 9
    return celcius


if __name__ == "__main__":
    print("What do you want to do? - input a number")
    print("1. Celcius to ahrenheit")
    print("2. Fahrenheit to Celcius")

    good_choice = False

    while not good_choice:
        try:
            opt = int(input())

            if opt == 1:
                celcius = float(input("Enter temperature in Celcius: "))
                fahrenheit = celcius2fahrenheit(celcius)
                print(f"{celcius}°C is equal to {fahrenheit}°F")
                good_choice = True
            elif opt == 2:
                fahrenheit = float(input("Enter temperature in Fahrenheit "))
                celcius = fahrenheit2celcius(fahrenheit)
                print(f"{fahrenheit}°F is equal to {celcius}°C")
                good_choice = True
            else:
                raise ValueError("Not a valid option")
        except Exception as e:
            print(f"Error: {e}")
            print("Try again")
