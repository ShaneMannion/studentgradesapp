from Grades import Grades
from Courses import Courses
from Enrollments import Enrollments

class GradingHelper:

    grades = Grades
    courses = Courses
    enrollments = Enrollments

    def __init__(self, grades, courses, enrollments):
        self.grades = grades
        self.courses = courses
        self.enrollments = enrollments
    
    def listGradesByStudentID(self, studentID):
        studentsGrades = []
        for currentEnrollment in self.enrollments.allEnrollments:
            currentStudentID = int(currentEnrollment.student_ID)
            if currentStudentID == studentID:
                for currentCourse in self.courses.allCourses:
                    if currentEnrollment.course_ID == currentCourse.course_ID:
                        for currentGrade in self.grades.allGrades:
                            if currentEnrollment.enrollment_ID == currentGrade.enrollment_ID:
                                studentGrade = [currentEnrollment.student_ID, currentCourse.course_Name, currentGrade.assignment_ID, currentGrade.mark]
                                studentsGrades.append(studentGrade)
        return studentsGrades