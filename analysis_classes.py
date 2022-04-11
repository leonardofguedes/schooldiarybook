from appstudent import students_classes


def analysis_classes():
    for n in students_classes:
        print(f'Class: {n}\n')
    return print(f'Your school have {len(students_classes)} registered class(es).')