
from Students import Students
from Enrollments import Enrollments
from EnrollmentHelper import EnrollmentHelper
import json


enrollments = Enrollments()
students = Students()
enrollmentHelper = EnrollmentHelper(enrollments, students)


def loadTestData():
    enrollments.allEnrollments.clear()
    enrollments.bulkLoad()
    students.bulkLoad()


def testListStudentsByCourseID():
    loadTestData()
    listOfStudents = enrollmentHelper.listStudentsByCourseID(2)
    assert ("Smith" in listOfStudents) == True
    assert ("Johnson" in listOfStudents) == True
#    print(listOfStudents)
#    expected_Data = """{
#  "response": "\n{\n    \"student_ID\": 1,\n    \"first_Name\": \"Ethan\",\n    \"surname\": \"Smith\",\n    \"date_Of_Birth\": \"2000-05-11\"\n}\n{\n    \"student_ID\": 2,\n    \"first_Name\": \"Olivia\",\n    \"surname\": \"Lee\",\n    \"date_Of_Birth\": \"1999-06-12\"\n}\n{\n    \"student_ID\": 5,\n    \"first_Name\": \"Noah\",\n    \"surname\": \"Johnson\",\n    \"date_Of_Birth\": \"1999-12-13\"\n}"
#}"""
 #   assert json.loads(listOfStudents) == expected_Data
    #assert len(enrollmentHelper.listStudentsByCourseID(1)) == 3



