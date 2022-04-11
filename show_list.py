from appstudent import students_total
from appteacher import teacher_total


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






