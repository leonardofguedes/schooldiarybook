from main import Students

students_total = []
students_classes = []
students_average = []

def add_student():

    try:
        add = str(input('Student name: ->')).strip().capitalize()
        if add == '':
            add = 'Unknow'
        add2 = int(input('Student age: ->'))
        if add2 == '':
            add2 = 0
        add3 = int(input('Student class: ->'))
        student = Students(add,add2,add3)
        student = student.__str__()
        students_total.append(student)
        if add3 in students_classes:
            pass
        else:
            students_classes.append(add3)
            students_average.append(int(add2))
    except:
        print('Due wrong info, the system will not add the student.')
        pass

