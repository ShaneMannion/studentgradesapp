class Course:

    course_ID = 0 
    course_Name = ""
    level = ""

    def __init__(self, course_ID, course_Name, level):
        self.course_ID = course_ID
        self.course_Name = course_Name
        self.level = level

    def getCourseName(self):
        return self.course_Name
