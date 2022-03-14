# defining a class Student
class Student:

    # defining its attributes
    def __init__(self):
        self.student_name = 'Albert'
        self.marks = 13


# printing original values

s = Student()
print(f'Original name: {s.student_name}\nOriginal marks: {s.marks}')

# modifying original values

s.student_name = 'Einstein'
s.marks = 56

print(f'Modified name: {s.student_name}\nModified marks: {s.marks}')
