from main import Teacher

teacher_total = []
subject = []
teachers_dict = {}

def add_teacher():

    add = str(input('Teacher name: ->')).strip().capitalize()
    add2 = str(input('Teacher subject: ->')).strip().capitalize()
    teachers_dict.update({add:add2})
    teacher = Teacher(add,add2)
    teacher = teacher.__str__()
    teacher_total.append(teacher)
    if add2 in subject:
        pass
    else:
        subject.append(add2)
