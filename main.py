class Students:
    def __init__(self, name, age, classs):
        self.name = name
        self.age = age
        self.classs = classs
        self.payment = True


    def __str__(self):
        return self.age, self.name, self.classs


class Classes:
    def __init__(self, teacher, subject, time):
        self.teacher = teacher
        self.subject = subject
        self.time = time


    def __str__(self):
        return self.teacher, self.subject, self.time
