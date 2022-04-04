from main import Students

students_total = []

def add_student():


    add = str(input('Student name: ->')).strip().capitalize()
    add2 = int(input('Student age: ->'))
    add3 = int(input('Student class: ->'))
    student = Students(add,add2,add3)
    student = student.__str__()
    students_total.append(student)


