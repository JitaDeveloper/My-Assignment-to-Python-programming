mydict = {
    'first': 23,
    'second': 34,
    'third': 16,
    'fourth': 66,
    'fifth': 20,
    'sixth': 18,
    'seventh': 25
}

values = []
for x in mydict:
    values.append(mydict[x])

print(f'Maximum: {max(values)}\nMinimum: {min(values)}')