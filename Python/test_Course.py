from Course import Course
import pytest

course_ID=1
course_Name="DevOps theory and practice"
level="Intermediate"


def testCreateCourseAndReturnName():
    course = Course(course_ID, course_Name, level)
    assert course.getCourseName() == course_Name