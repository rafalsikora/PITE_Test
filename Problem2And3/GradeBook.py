from Student import *
from Subject import *

class GradeBook:

    def __init__(self):
        self.listOfStudents = []

    def loadFromFile(self, name):
        assert isinstance(name, str)
        file = open(name)
        input = file.read()
        splitted = str.split(input, '\n')
        for entry in splitted:
            entrySplitted = str.split(entry, ', ')
            if len(entrySplitted) == 1:
                continue
            surname = entrySplitted[0]
            name = entrySplitted[1]
            student = Student(name, surname)
            subentries = entrySplitted[2:]
            for sub in subentries:
                subentrySplitted = str.split(sub, ' ')
                subject = Subject(subentrySplitted[0])
                for grade in subentrySplitted[1:]:
                    subject.AddGrade(float(grade))
                student.AddSubject(subject)
            self.listOfStudents.append(student)
        file.close()

    def getListOfStudents(self):
        return self.listOfStudents