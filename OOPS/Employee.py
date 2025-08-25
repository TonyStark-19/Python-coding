# This code creates employee class and enginner class which inherits properties from employee class

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role :", self.role)
        print("dept :", self.dept)
        print("salary :", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Enginner", "IT" ,"75,000")

eng1 = Engineer("Rahul kumar", "30")

eng1.showDetails()