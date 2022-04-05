from appstudent import students_total, students_classes, students_average
from appteacher import teacher_total


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
            return print(f'Your school have {len(students_total)} students.')
        if ask == 2:
            return print(f'Your classes are {students_classes}.')
        if ask == 3:
            return print(f'The average age of students is {round(sum(students_average)/len(students_average),1)} years')
        else:
            print('You have to choose [1], [2] or [3].')



def analysis_classes():
    return print(f'Your school have {len(class_total)} classes.')
