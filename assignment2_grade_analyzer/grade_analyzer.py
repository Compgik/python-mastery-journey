number = int(input('Enter any number:'))
if number % 2 == 0:
    print('Number entered is EVEN!')
else:
    print('Number entered is ODD')

if number > 0:
    print('Number entered is positive!')
elif number < 0:
    print('Number entered is negative!')
else:
    print('Number entered is ZERO!')
