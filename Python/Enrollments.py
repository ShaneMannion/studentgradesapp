from Enrollment import Enrollment
import csv
from Utilities import Utilities

class Enrollments:
    
    allEnrollments = []

    def addEnrollment(self, enrollment):
        if enrollment.enrollment_ID > 0:
            self.allEnrollments.append(enrollment)
            return True
        else:
            return False

    
    def bulkLoad(self, conn = None):
        rowCounter = 0
        if Utilities.isItTest():
            with open('./../TestData/SampleEnrollmentData.csv', 'r') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                try: 
                    for row in readCSV:
                        rowCounter = rowCounter +1
                        if rowCounter > 1:
                            enrollment_ID= row[0]
                            course_ID= row[1]
                            student_ID=row[2]
                            enrollment = Enrollment(enrollment_ID, course_ID, student_ID)
                            #TODO - add a null check and reset here?
                            self.allEnrollments.append(enrollment)
                            lastRow = row
                        else:
                            print("RowCounter !> 1")
                except:
                    print("**{0}**".format(lastRow))
        else: 
            cur = conn.cursor()
            cur.execute("SELECT * FROM Enrollments")
            for (enrollment_id, course_id, student_id) in cur:
                enrollment = Enrollment(enrollment_id, course_id, student_id)
                self.allEnrollments.append(enrollment) 
        return len(self.allEnrollments)
