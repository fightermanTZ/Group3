def student_info(name="Frido", age=20, gpa=3):
    print(f"Student name is {name}, {age} years old with a Gpa of {gpa}")

student_info("Nyinondi", 20, 4)
student_info(name="Angel", age=20, gpa=4)
student_info()

def student_info1(*args, marks):
    total=sum(marks)
    print(f"Student marks are {total}")
student_info1(marks=[20,34,45,50])

def student_info2(*args, name,):
    print(f'Student name is {name}')
student_info2(name="fridolin")
