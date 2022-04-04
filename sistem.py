from appstudent import add_student, students_total
from appclass import add_class, class_total

def welcome():
    call = str(input('What do you want to add? [Class][Student]')).strip().capitalize()
    if call == 'Student' or call == 'Class':
        if call == 'Student':
            add_student()
        if call == 'Class':
            add_class()
    else:
        print('Wrong answer.')



def show():
    ask = str(input('Do you want to see a list of Students or Classes? [Y][N]')).upper().strip()
    if ask == 'Y':
        ask2 = str(input('Which one?')).strip().capitalize()
        if ask2 == 'Students' or ask2 == 'Classes':
            if ask2 == 'Students':
                print(students_total)
            if ask2 == 'Classes':
                print(class_total)
        else:
            print('Wrong answer.')
    else:
        pass

def tela():
    while True:
        welcome()
        show()
        con = str(input('Continue? -> [Y][N]')).strip().upper()
        if con == 'N':
            break


