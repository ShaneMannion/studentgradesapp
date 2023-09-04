class Enrollment:

    enrollment_ID = 0 
    course_ID = ""
    student_ID = ""

    def __init__(self, enrollment_ID, course_ID, student_ID):
        self.enrollment_ID = enrollment_ID
        self.course_ID = course_ID
        self.student_ID = student_ID

    def getEnrollmentDetails(self, enrollment_ID):
        return self.course_ID, self.student_ID
