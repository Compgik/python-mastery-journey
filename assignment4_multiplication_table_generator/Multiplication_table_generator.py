while True:
    number = int(input('Enter a number:'))
    print(f'\nMultiplication table for {number}')
    print('-' * 30)

    for i in range(1, 13):
        result = number * i
        print(f'{number} * {i} = {result}')
    print('-' * 30)
    again = input('Do you want another table?(yes/no)')
    if again != 'yes':
        print("Goodbye!!")
        break
