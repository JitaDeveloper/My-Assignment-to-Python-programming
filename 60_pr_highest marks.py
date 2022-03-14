def student(name, roll, marks):
    return name, roll, marks


stud = []
stud.append(student('John', 101, 45))
stud.append(student('Clare', 102, 55))
stud.append(student('Derek', 103, 47))
stud.append(student('Shiva', 104, 30))
stud.append(student('Libra', 105, 36))
stud.append(student('Kiwi', 106, 55))
stud.append(student('Cancer', 107, 51))
stud.append(student('Edmund', 108, 55))

marks = []
for i in range(len(stud)):
    marks.append(stud[i][-1])

first_boys = []
for i in range(len(stud)):
    if stud[i][-1] == max(marks):
        first_boys.append(stud[i][0])

print(f"First boys are {', '.join(first_boys)} with {max(marks)} marks!")
