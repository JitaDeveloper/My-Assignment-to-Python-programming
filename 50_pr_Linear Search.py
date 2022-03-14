numbers = ['John', 1, 2, 3, 4, 5, 'Rabbit', 3]
v = eval(input('Find: '))

if v in numbers:
    print(f'{v} is in list')
    print(f'Position of first occurrence is: {numbers.index(v)}')
else:
    print(f'{v} is not in list')

