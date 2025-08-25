# This code takes student's name and marks of five subjects and prints the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for el in self.marks:
            sum += el
        print("Hi", self.name, "your average score is :", sum/5)
    
s1 = Student("Aditya", [94, 88, 89, 89, 65])

s1.get_average()