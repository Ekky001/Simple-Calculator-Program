def calculator():
    print("Welcome to the Simple Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Choose an operation: 1 (+), 2 (-), 3 (*), 4 (/)")
        choice = input("Enter your choice (1/2/3/4): ")
        
        # Perform operation based on user choice
        if choice == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Invalid choice. Please select a valid operation.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator function
calculator()
