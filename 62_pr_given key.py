mydict = {
    'first': 23,
    'second': 34,
    'third': 16,
    'fourth': 66,
    'fifth': 20,
    'sixth': 18,
    'seventh': 25
}

while True:
    query = eval(input('Find key: '))
    if mydict.get(query) is None:
        print(f"Key {query} doesn't exist")
        exit()
    else:
        print(f"Key {query} exists")
