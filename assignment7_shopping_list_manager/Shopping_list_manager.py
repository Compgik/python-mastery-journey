shopping_list = []

while True:
    print('---Shopping List Menu---')
    print('1. Add item')
    print('2. View list')
    print('3. Remove item')
    print('4. Exit')
    choice = input('Enter your choice (1-4): ')

    if choice == '1':
        item = input('Enter item to add: ')
        shopping_list.append(item)
        print(f'{item} added to your list!')

    elif choice == '2':
        if len(shopping_list) == 0:
            print('Your list is empty.')
        else:
            print(shopping_list)
            for x in shopping_list:
                print('-', x)

    elif choice == '3':
        item = input('Enter item to remove: ')
        if item in shopping_list:
            shopping_list.remove(item)
            print(f'{item} removed from your list.')
        else:
            print('That item is not in your list.')

    elif choice == '4':
        print('Goodbye')
        break

    else:
        print('Invalid option,try again!')
