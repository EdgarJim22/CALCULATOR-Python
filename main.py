# main.py

from functions import calculate

# Main function that interacts with the user
def main():
    print("Welcome to the Basic Calculator!")
    print("Options:")
    print("1 for addition (+)")
    print("2 for subtraction (-)")
    print("3 for multiplication (*)")
    print("4 for division (/)")
    print("Type '5' to quit the calculator.")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (1, 2, 3, 4) or '5' to quit: ")
            if operator == '5':
                print("Exiting the calculator. Goodbye!")
                break

            operator_map = {'1': '+', '2': '-', '3': '*', '4': '/'}
            if operator in operator_map:
                operator_symbol = operator_map[operator]
                num2 = float(input("Enter the second number: "))
                result = calculate(num1, operator_symbol, num2)
                print(f"The result is: {result}")
            else:
                print("Invalid input. Please enter 1, 2, 3, 4, or 5.")
        except ValueError:
            print("Invalid number entered. Please enter a valid number.")

if __name__ == "__main__":
    main()
