import math
import json


def show_menu():
    print("\n" + "=" * 35)
    print("     SCIENTIFIC CALCULATOR")
    print("     Made by:SINA BANIASADI")
    print("=" * 35)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm (log)")
    print("11. Natural Logarithm (In)")
    print("12. Factorial (!)")
    print("13. Calculator History")
    print("14. Clear History")
    print("0. Exit")
    print("=" * 35)


def load_history():
    try:
        with open("history.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_history(history):
    with open("history.json","w")as file:
        json.dump(history,file,indent=4)


def main():
    history = load_history()
    while True:
        show_menu()
        choice = input("choose an operation?")

        if choice == "0":
            print("calculater closed!")
            break

        try:
            if choice in ["1", "2", "3", "4", "5"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second numer: "))

                if choice == "1":
                    result = num1 + num2

                elif choice == "2":
                    result = num1 - num2

                elif choice == "3":
                    result = num1 * num2

                elif choice == "4":
                    if num2 == 0:
                        print("Error cannot divide by zero!")
                        continue
                    result = num1 / num2

                else:
                    result = num1 ** num2

            elif choice == "6":
                num = float(input("Enter number: "))
                if num < 0:
                    print("Error Negative number!")
                    continue
                result = math.sqrt(num)

            elif choice in ["7", "8", "9"]:
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)
                if choice == "7":
                    result = math.sin(radians)

                elif choice == "8":
                    result = math.cos(radians)

                else:
                    if math.isclose(math.cos(radians), 0, abs_tol=1e-12):
                        print("Error: Tangent is underfinde!")
                        continue
                    result = math.tan(radians)

            elif choice == "10":
                num = float(input("Enter number: "))
                if num <= 0:
                    print("Error Number must be positive!")
                    continue
                result = math.log10(num)

            elif choice == "11":
                num = float(input("Enter number: "))
                if num <= 0:
                    print("Error Number must be positive!")
                    continue
                result = math.log(num)

            elif choice == "12":
                num = int(input("Enter a non-negative intger: "))
                if num < 0:
                    print("Error Number cannot be negative!")
                    continue
                result = math.factorial(num)
                 
            elif choice == "13":
                if not history:
                    print("History is empty!")
                else:
                    for item in history:
                        print(f"Operation:{item['operation']} | Result:{item['result']}")
                continue
            
            elif choice == "14":
                confrim = input("Are you sure you want to clear history? (y/n): ")
                if confrim.lower() == "y":
                    history.clear()
                    save_history(history)
                    print("History cleared successfully!")
                else:
                    print("History was not cleared!")
                continue
            else:
                print("Invalid choice!")
                continue

            print(f"Result: {result}")
            
            history.append({
                "operation":choice,
                "result":result
            })
            save_history(history)

        except ValueError:
            print("Error please enter a valid number!")
        except OverflowError:
            print("Error number is too large!")


if __name__ == "__main__":
    main()
