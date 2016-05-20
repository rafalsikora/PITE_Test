class Subject:

    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name
        self.gradeList = []

    def AddGrade(self, grade):
        assert isinstance(grade, (int, float))
        self.gradeList.append(grade)

    def getListOfGrades(self):
        return self.gradeList

    def getName(self):
        return self.name