from appstudent import add_student, students_total
from appteacher import add_teacher, teacher_total
from analysis import analysis_student, analysis_classes,show_list

def welcome():
    while True:
        call = str(input('What do you want to add? [Teacher][Student][End adding]')).strip().capitalize()
        if call == 'Student' or call == 'Teacher':
            if call == 'Student':
                add_student()
            if call == 'Teacher':
                add_teacher()
        else:
            break


def analy():
    while True:
        q = str(input('Do you want to analyze the added numbers? [Y][N]')).strip().upper()
        if q == 'Y':
            while True:
                q1 = str(input('Classes[CL]| Students[ST]| Teachers[TE]')).upper().strip()
                if q1 == 'CL':
                    analysis_classes()
                if q1 == 'ST':
                    analysis_student()
                if q1 == 'TE':
                    pass
                else:
                    break
        else:
            break


def tela():
    while True:
        welcome()
        show_list()
        analy()
        con = str(input('Continue with adding? -> [Y][N]')).strip().upper()
        if con == 'N':
            break


