from main import Classes

class_total = []

def add_class():

    add = str(input('Teacher name: ->')).strip().capitalize()
    add2 = str(input('Teacher subject: ->')).strip().capitalize()
    add3 = int(input('Class time: ->'))
    teacher = Classes(add,add2,add3)
    teacher = teacher.__str__()
    class_total.append(teacher)
