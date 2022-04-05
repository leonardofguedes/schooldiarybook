from main import Students

students_total = []
students_classes = []
students_average = []

def add_student():


    add = str(input('Student name: ->')).strip().capitalize()
    if add == '':
        add = 'Unknow'
    add2 = input('Student age: ->')
    if add2 == '':
        add2 = 0
    add3 = input('Student class: ->')
    if add3 == '':
        add3 = 'Unknow'
    student = Students(add,add2,add3)
    student = student.__str__()
    students_total.append(student)
    students_classes.append(add3)
    students_average.append(int(add2))
