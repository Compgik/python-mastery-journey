while True:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number:'))
    operation = input('Enter the operation (+, -, *, /):')

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
        continue
    print(f'The result of {num1} {operation} {num2} = {result}')

    again = input('Do you want to calculate again? (yes/no)').lower()
    if again != 'yes':
        print('Goodbye!')
        break
