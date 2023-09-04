from Enrollments import Enrollments
from Students import Students
import json

class EnrollmentHelper:

    enrollments = Enrollments
    students = Students

    def __init__(self, enrollments, students):
        self.enrollments = enrollments
        self.students = students
    
    def listStudentsByCourseID(self, courseID):
        enrolledStudents = []
        json_string=""

        for currentEnrollment in self.enrollments.allEnrollments:
            currentCourseID = int(currentEnrollment.course_ID)
            if currentCourseID == courseID:
                for currentStudent in self.students.allStudents:
                    if currentStudent.student_ID == currentEnrollment.student_ID:
                        enrolledStudents.append(currentStudent)

        for enrolledStudent in enrolledStudents:
            json_data = enrolledStudent.student_to_dict()
            # Build the JSON string
            json_string = json_string + '\n' + json.dumps(json_data, indent=4, default=str)
        print(json_string)

        return json_string
