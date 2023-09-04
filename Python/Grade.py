class Grade:

    enrollment_ID = 0 
    assignment_ID = 0
    mark = 0

    def __init__(self, enrollment_ID, assignment_ID, mark):
        self.enrollment_ID = enrollment_ID
        self.assignment_ID = assignment_ID
        self.mark = mark

    def getGradeDetails(self, enrollment_ID, assignment_ID):
        return self.mark
