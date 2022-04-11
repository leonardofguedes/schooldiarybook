from appstudent import students_total, students_classes, students_average
import statistics


def analysis_student():
    while True:
        print('Do you want to know:\n[Number of students]\n[Classes of students]\n[Average age of students]')
        ask = int(input('Option [1][2][3]'))
        if ask == 1:
            print(f'Your school have {len(students_total)} student(s).')
            break
        if ask == 2:
            if len(students_classes) == 0:
                print('You do not have registered classes.')
                break
            else:
                print(f'Your registered class(es) is(are) {students_classes}.')
                break
        if ask == 3:
            if len(students_total) == 0:
                return print('You do not have registered students.')
            else:
                print(f'The average age of registered student(s) is {round(statistics.mean(students_average),1)} years')
                ask = str(input('Do you want to know how many students are above the average age? [Y][N]')).upper().strip()
                if ask == 'Y':
                    res = filter(lambda x: x > statistics.mean(students_average), students_average)
                    print(f'{len(list(res))} student(s)')
                    break
                else:
                    break
        elif ask > 3:
            print('You have to choose [1], [2] or [3].')