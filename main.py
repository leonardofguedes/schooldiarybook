class Students:
    def __init__(self, name='Unknow', age=0, classs=0):
        self.name = name
        self.age = age
        self.classs = classs
        self.payment = True


    def __str__(self):
        return self.name, self.age, self.classs


class Teacher:
    def __init__(self, teacher, subject):
        self.teacher = teacher
        self.subject = subject


    def __str__(self):
        return self.teacher, self.subject
