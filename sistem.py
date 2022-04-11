from appstudent import add_student
from appteacher import add_teacher
from show_list import show_list
from analysis_student import analysis_student
from analysis_classes import analysis_classes
from analysis_teacher import analysis_teachers

def welcome():
    while True:
        try:
            call = str(input('What do you want to add? [Teacher][Student][End adding]')).strip().capitalize()
            if call == 'Student' or call == 'Teacher':
                if call == 'Student':
                    add_student()
                if call == 'Teacher':
                    add_teacher()
            elif call == 'End adding':
                break
            else:
                print('Wrong option.')
        except:
              break



def analy():
    while True:
        try:
            q = str(input('Do you want to analyze the added numbers? [Y][N]')).strip().upper()
            if q == 'Y':
                while True:
                    q1 = str(input('Classes[CL]| Students[ST]| Teachers[TE]')).upper().strip()
                    if q1 == 'CL':
                        analysis_classes()
                        break
                    if q1 == 'ST':
                        analysis_student()
                        break
                    if q1 == 'TE':
                        analysis_teachers()
                        break
            elif q == 'N':
                break
        except:
            break


def tela():
    while True:
        welcome()
        show_list()
        analy()
        con = str(input('Continue with adding? -> [Y][N]')).strip().upper()
        if con == 'N':
            break


