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
    
    def listGradesByStudentID(self, student_id):
        studentsGrades = []
        for currentEnrollment in self.enrollments.allEnrollments:
            currentStudentID = int(currentEnrollment.student_id)
            if currentStudentID == student_id:
                for currentCourse in self.courses.allCourses:
                    if currentEnrollment.course_id == currentCourse.course_id:
                        for currentGrade in self.grades.allGrades:
                            if currentEnrollment.enrollment_id == currentGrade.enrollment_id:
                                studentGrade = [currentEnrollment.student_id, currentCourse.course_name, currentGrade.assignment_id, currentGrade.mark]
                                studentsGrades.append(studentGrade)
        return studentsGrades