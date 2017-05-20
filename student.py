class Student:


    def __init__(self,name, number, marks):
        self.name= name
        self.number= number
        self.marks=marks


    def __str__(self):
        return "STUDENT: " + self.name + " NUMBER: " + str(self.number) + " MARKS: "+ str(self.marks)
