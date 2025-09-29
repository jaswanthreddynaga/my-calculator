from operations import add, subtract, multiply, divide

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def get_operation():
    while True:
        op = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip().lower()
        if op in ['+', '-', '*', '/', 'exit']:
            return op
        else:
            print("Invalid operation. Please choose from +, -, *, /.")

def main():
    print("Welcome to the command-line calculator!")
    while True:
        operation = get_operation()
        if operation == 'exit':
            print("Goodbye!")
            break
    
        num1, num2 = get_numbers()
    
        try:
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            
            print(f"Result: {result}\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
