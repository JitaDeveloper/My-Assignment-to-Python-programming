numbers = ['John', 1, 2, 3, 4, 5, 'Rabbit', 3]
old = numbers.copy()

# modify the old list

numbers[2] = 'John'
numbers.append(7)
numbers.insert(3, 'Google')
numbers.remove(4)
numbers.pop()
print(f'The modified list is: {numbers}')

print(f'The old list was: {old}')