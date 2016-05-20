from GradeBook import *
import GradeBookAnalysis

gb = GradeBook()
gb.loadFromFile('gradeBook.txt')

GradeBookAnalysis.storeAverageInFile(gb, "averageGrades.txt")