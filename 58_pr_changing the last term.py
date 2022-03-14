n_tuples = [
    (5, 2, 79),
    (15, 10, 43, 27),
    (14, 7, 16),
    (45, 5, 89, 6, 17, 22)
]

final = []
for i in range(len(n_tuples)):
    new_list = list(n_tuples[i])
    new_list[-1] = 100
    final.append(tuple(new_list))

print(final)