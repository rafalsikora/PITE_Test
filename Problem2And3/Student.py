class Student:

    def __init__(self, firstName, lastName):
        assert isinstance(firstName, str)
        assert isinstance(lastName, str)
        self.firstName = firstName
        self.lastName = lastName
        self.listOfSubjects = []

    def AddSubject(self, name):
        self.listOfSubjects.append(name)

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getListOfSubjects(self):
        return self.listOfSubjects
