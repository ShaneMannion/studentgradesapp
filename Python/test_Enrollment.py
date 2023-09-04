from Enrollment import Enrollment
import pytest

enrollment_ID=1
course_ID=2
student_ID=3


def testCreateEnrollmentAndReturnDeatils():
    enrollment = Enrollment(enrollment_ID, course_ID, student_ID)
    enrolledCourseID, enrolledStudentID = enrollment.getEnrollmentDetails(enrollment_ID)

    assert enrolledCourseID == course_ID
    assert enrolledStudentID == student_ID