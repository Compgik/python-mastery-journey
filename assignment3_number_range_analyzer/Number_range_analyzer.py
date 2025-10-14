start = int(input('Enter start number: '))
end = int(input('Enter end number: '))

print(f'Analyzing numbers between {start} and {end}!')

for number in range(start, end + 1):
    if number % 2 == 0:
        parity = 'EVEN'
    else:
        parity = 'ODD'

    if number > 0:
        sign = 'POSITIVE'
    elif number < 0:
        sign = 'NEGATIVE'
    else:
        sign = 'ZERO'

    print(f'Number: {number} is {parity} and {sign}')
