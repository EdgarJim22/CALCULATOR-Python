# main.py

from calculator.functions import calculate

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
        # Prompt the user for the first number
        num1 = float(input("Enter the first number: "))
        
        # Prompt the user for the operator
        operator = input("Enter an operator (1, 2, 3, 4) or '5' to quit: ")
        
        # Check if the user wants to exit
        if operator == '5':
            print("Exiting the calculator. Goodbye!")
            break  # Exit the loop if the user wants to quit
        
        # Map numbers to operators
        operator_map = {'1': '+', '2': '-', '3': '*', '4': '/'}
        if operator in operator_map:
            operator_symbol = operator_map[operator]
            # Prompt the user for the second number
            num2 = float(input("Enter the second number: "))
            
            # Calculate the result and display it
            result = calculate(num1, operator_symbol, num2)
            print(f"The result is: {result}")
        else:
            print("Invalid input. Please enter 1, 2, 3, 4, or 5.")

# Run the main function if the script is being run directly
if __name__ == "__main__":
    main()
