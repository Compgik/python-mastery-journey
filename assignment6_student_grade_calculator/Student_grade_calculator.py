subjects = ['Math:', 'English:', 'Science:', 'History:', 'ICT:']

while True:
    marks = []

    for x in subjects:
        score = int(input(f'{x}'))
        marks.append(score)

    total = sum(marks)
    average = total / len(marks)
    print(f'Total marks:{total}')
    print(f'Average mark:{average}')

    if average >= 80:
        Grade = 'A'
    elif average >= 70:
        Grade = 'B'
    elif average >= 60:
        Grade = 'C'
    elif average >= 50:
        Grade = 'D'
    else:
        Grade = 'Fail'
    print(f'Grade: {Grade}')

    again = input('Do you want to calculate marks again?(yes/no)')
    if again != 'yes':
        break
