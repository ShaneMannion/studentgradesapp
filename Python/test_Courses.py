import csv
from Course import Course
from Courses import Courses
import pytest


courses = Courses()

def testBulkLoadCourses():
    # clear doesn't work  ====>>>>    Courses.clearCoursesData()
    assert courses.bulkLoad() == 12

def testAddOneCourse():
    course = Course(1,"Introduction to Python", "Novice")
    assert courses.addCourse(course) == True

