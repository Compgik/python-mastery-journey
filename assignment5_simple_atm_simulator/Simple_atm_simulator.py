balance = 0
pin = '1234'

for tries in range(3):
    login = input('Please enter pin:')
    if login == pin:
        print('login successfuly!!')
        break
    else:
        print("You have entered wrong pin!")
else:
    print('Account blocked!')
    exit()

while True:
    print('\n---ATM Menu---')
    print('1. Check Balance')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Exit')

    choice = input('Enter option:')
    if choice == '1':
        print(f'Your account balance is {balance}')
    elif choice == '2':
        amount = int(input('Enter deposit amount:'))
        balance += amount
        print(f'{amount} deposited successfuly!')
    elif choice == '3':
        amount = int(input('Enter withdrawal amount:'))
        if amount > balance:
            print('Insufficient balance!')
        else:
            balance -= amount
            print(f'{amount} withdrawn successfuly!')
    elif choice == '4':
        print('Thank you for using our ATM!')
        break
    else:
        print('Invalid option try again!')
