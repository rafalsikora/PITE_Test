from GradeBook import *
import numpy

def storeAverageInFile(gb, outputName):
    assert isinstance(gb, GradeBook)
    assert isinstance(outputName, str)
    listOfStudents = gb.getListOfStudents()

    file = open(outputName, 'w')

    for student in listOfStudents:
        file.write('\n--------------\n')
        file.write(student.getFirstName()+" "+student.getLastName()+"\n")
        subjects = student.getListOfSubjects()
        for subject in subjects:
            file.write(subject.getName()+" ")
            listOfGrades = subject.getListOfGrades()
            mean = numpy.average(listOfGrades)
            file.write(str(mean)+"\n")
    file.close()