l = [45, 78, 14, 6, 10]

print(f'List converted to tuple: {tuple(l)}')

# List of n tuples

n_tuples = [
    (5, 2, 79),
    (15, 10, 43, 27),
    (14, 7, 16),
    (45, 5, 89, 6, 17, 22)
]

second = []
for i in range(len(n_tuples)):
    second.append(n_tuples[i][1])

second.sort()
new_list = []
for i in second:
    for j in range(len(n_tuples)):
        if n_tuples[j][1] == i:
            new_list.append(n_tuples[j])

print(new_list)