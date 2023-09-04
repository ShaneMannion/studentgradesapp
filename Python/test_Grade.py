from Grade import Grade
import pytest

enrollment_ID=1
assignment_ID=2
mark=80


def testCreateGradeAndReturnDetails():
    grade = Grade(enrollment_ID, assignment_ID, mark)
    gradedMark = grade.getGradeDetails(enrollment_ID, assignment_ID)

    assert gradedMark == mark