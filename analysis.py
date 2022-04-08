from appstudent import students_total, students_classes, students_average
from appteacher import teacher_total, subject
import statistics

def show_list():
    while True:
        try:
            ask = str(input('Do you want to see a list of Students or Teachers? [Y][N]')).upper().strip()
            if ask == 'Y':
                ask2 = str(input('Which one?')).strip().capitalize()
                if ask2 == 'Students' or ask2 == 'Teachers':
                    if ask2 == 'Students':
                        if len(students_total) == 0:
                            print('You do not have registered students.')
                        else:
                            print(f'The list of students\n{students_total}')
                    if ask2 == 'Teachers':
                        if len(teacher_total) == 0:
                            print('You do not have registered teachers.')
                        else:
                            print(f'The list of teachers\n{teacher_total}')
                else:
                    print('Wrong option. Write Students or Teachers.')
            elif ask == 'N':
                    break
            elif ask != 'N' and ask != 'Y':
                print('Wrong option. Choose Y or N.')
        except:
            print('Wrong option.')



def analysis_student():
    while True:
        print('Do you want to know:\n[Number of students]\n[Classes of students]\n[Average age of students]')
        ask = int(input('Option [1][2][3]'))
        if ask == 1:
            return print(f'Your school have {len(students_total)} student(s).')
            break
        if ask == 2:
            if len(students_classes) == 0:
                print('You do not have registered classes.')
                break
            else:
                return print(f'Your registered class(es) is(are) {students_classes}.')
                break
        if ask == 3:
            if len(students_total) == 0:
                return print('You do not have registered students.')
            else:
                print(f'The average age of registered student(s) is {round(statistics.mean(students_average),1)} years')
                ask = str(input('Do you want to know how many students are above the average age? [Y][N]')).upper().strip()
                if ask == 'Y':
                    res = filter(lambda x: x > statistics.mean(students_average), students_average)
                    return print(f'{len(list(res))} student(s)')
                    break
                else:
                    break
        elif ask > 3:
            print('You have to choose [1], [2] or [3].')


def analysis_classes():
    for n in students_classes:
        print(f'Class: {n}\n')
    return print(f'Your school have {len(students_classes)} registered class(es).')


def analysis_teachers():
    for n in subject:
        print(f'Subject: {n}\n')
    return print(f'Your school have {len(subject)} subject(s) and {len(teacher_total)} teacher(s).')
