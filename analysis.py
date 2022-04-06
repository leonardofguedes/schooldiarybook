from appstudent import students_total, students_classes, students_average
from appteacher import teacher_total, subject
import statistics

def show_list():
    while True:
        ask = str(input('Do you want to see a list of Students or Teachers? [Y][N]')).upper().strip()
        if ask == 'Y':
            ask2 = str(input('Which one?')).strip().capitalize()
            if ask2 == 'Students' or ask2 == 'Teachers':
                if ask2 == 'Students':
                    print(f'The list of students\n{students_total}')
                    break
                if ask2 == 'Teachers':
                    print(f'The list of teachers\n{teacher_total}')
                    break
            else:
                print('Wrong answer.')
        else:
            break



def analysis_student():
    while True:
        print('Do you want to know:\n[Number of students]\n[Classes of students]\n[Average age of students]')
        ask = int(input('Option [1][2][3]'))
        if ask == 1:
            return print(f'Your school have {len(students_total)} student(s).')
        if ask == 2:
            return print(f'Your registered class(es) is(are) {students_classes}.')
        if ask == 3:
            print(f'The average age of registered student(s) is {round(statistics.mean(students_average),1)} years')
            ask = str(input('Do you want to know how many students are above the average age? [Y][N]')).upper().strip()
            if ask == 'Y':
                res = filter(lambda x: x > statistics.mean(students_average), students_average)
                return print(f'{len(list(res))} student(s)')
            else:
                break

        else:
            print('You have to choose [1], [2] or [3].')


def analysis_classes():
    for n in students_classes:
        print(f'Class: {n}\n')
    return print(f'Your school have {len(students_classes)} registered class(es).')


def analysis_teachers():
    for n in subject:
        print(f'Subject: {n}\n')
    return print(f'Your school have {len(subject)} subject(s) and {len(teacher_total)} teacher(s).')
