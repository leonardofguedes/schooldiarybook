from appteacher import teacher_total, subject, teachers_dict

def analysis_teachers():
    for n in subject:
        print(f'Subject: {n}\n')
    print(f'Your school have {len(subject)} subject(s) and {len(teacher_total)} teacher(s).')
    try:
        teacher_consult = str(input('Do you want to consult the subject of a teacher? -> [Y][N]')).upper().strip()
        if teacher_consult == 'Y':
            name_teacher_consult = str(input('Teacher name: ->')).strip().capitalize()
            if name_teacher_consult in teachers_dict.keys():
                print(f'The subject of teacher {name_teacher_consult} is {teachers_dict.get(name_teacher_consult)}.')
            else:
                print(f'Sorry. I did not found {name_teacher_consult} here.')
        else:
            pass
    except:
        print('Error')


