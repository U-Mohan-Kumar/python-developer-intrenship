def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Thank you! Exiting...")
            break
        if choice in ['1', '2', '3', '4']:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
        

            if choice == '1':
                result = add(x, y)
            elif choice == '2':
                result = subtract(x, y)
            elif choice == '3':
                result = multiply(x, y)
            elif choice == '4':
                result = divide(x, y)

            print("Result:", result)
        else:
            print("Invalid option. Try again!")
calculator()