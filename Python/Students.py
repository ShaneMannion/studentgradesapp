from Student import Student
import csv
from Utilities import Utilities

pytest = False

class Students:

    allStudents = []

    def addStudent(self, student):
        if student.student_ID > 0:
            self.allStudents.append(student)
            return True
        else:
            return False
    
    def bulkLoad(self, conn = None):
        rowCounter = 0
        if Utilities.isItTest():
            with open('./../TestData/SampleStudentData.csv', 'r') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                try: 
                    for row in readCSV:
                        rowCounter = rowCounter +1
                        if rowCounter > 1:
                            student_ID= row[0]
                            first_Name= row[1]
                            surname=row[2]
                            date_Of_Birth=row[3]
                            student = Student(student_ID, first_Name, surname, date_Of_Birth)
                            #TODO - add a null check and reset here?
                            self.allStudents.append(student)
                            lastRow = row
                        else:
                            print("RowCounter !> 1")
                except:
                    print("**{0}**".format(lastRow))
        else: 
            cur = conn.cursor()
            cur.execute("SELECT * FROM Students")
            for (Student_ID, First_Name, Surname, Date_Of_Birth) in cur:
                student = Student(Student_ID, First_Name, Surname, Date_Of_Birth)
                self.allStudents.append(student)
        return len(self.allStudents)

    def countStudents(self):
        studentCount = len(self.allStudents)
        print ("length {0}".format(studentCount))
        return len(self.allStudents)

    def clearStudentsData(self):
        print ("Before Clear {0} rows".format(len(self.allStudents)))
        self.allStudents.clear
        print ("After Clear {0} rows".format(len(self.allStudents)))