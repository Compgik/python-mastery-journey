def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


while True:
    print('---Python Calculator---')
    print('1. Add')
    print('2. Subtract')
    print('3. Miltiply')
    print('4. Divide')
    print('5. Exit')

    choice = input('Enter your choice: ')

    if choice in ['1', '2', '3', '4']:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number:'))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        print(f'Result: {result}')

    elif choice == '5':
        print('Goodbye!')
        break

else:
    print('Choice please try again!')
