from operator import add

class Student:
    def __init__(self, lastname, name, father):
        self.lastname = lastname
        self.name = name
        self.father = father
        self.arr_marks = []

    def __add__(self, mark):
        self.arr_marks.append(mark)

    @property
    def full_name(self):
        return f'{self.lastname} {self.name} {self.father}'

    def __str__(self):
        return f'{self.full_name} {self.arr_marks}'


class Group:
    def __init__(self):
        self.students = []
        self.index = 0

    def __add__(self, student):
        self.students.append(student)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.students):
            self.index=0
            raise StopIteration
        index = self.index
        self.index += 1
        return self.students[index]


import csv

def import_from(file, line, s):
    with open(file, 'r') as task1:
        csv_reader1 = csv.reader(task1)
        for l in csv_reader1:
            if line[0] == l[0] and line[1] == l[1] and line[2] == l[2]:
                s + int(l[3])

group = Group()
with open('students.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        s = Student(line[0], line[1], line[2])
        import_from('task1.csv', line, s)
        import_from('task2.csv', line, s)
#        import_from('task3.csv', line, s)
        if len(s.arr_marks) != 2:
            for _ in range(3-len(s.arr_marks)):
                s+0
        group + s

print("--------task3-------")
for person in group:
    print(person)

print("--------task4-------")
for student in group:
    if 0 not in student.arr_marks:
        high_mark = max(student.arr_marks)
        print(f'{student.full_name} {high_mark}')