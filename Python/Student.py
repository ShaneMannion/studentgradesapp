class Student:

    student_ID=0
    first_Name="" 
    surname=""
    date_Of_Birth=""

    def __init__(self, student_ID, first_Name, surname, date_Of_Birth):
        self.student_ID = student_ID
        self.first_Name = first_Name
        self.surname = surname
        self.date_Of_Birth = date_Of_Birth

    def getSurname(self):
        return self.surname

    def student_to_dict(self):
        return {"student_ID": self.student_ID, "first_Name": self.first_Name, "surname": self.surname, "date_Of_Birth": self.date_Of_Birth}