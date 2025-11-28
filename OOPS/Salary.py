# This program demonstrates the use of abstract classes.

# import abstract base class (ABC) and abstract class decorator
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def calculate_salary(self):
        print(f"Intern {self.name}'s salary is: ₹{self.stipend}")

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        print(f"Full-Time Employee {self.name}'s salary is: ₹{self.monthly_salary}")

class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        salary = self.hourly_rate * self.hours_worked
        print(f"Contract Employee {self.name}'s salary is: ₹{salary}")

# Creating objects
intern = Intern("Aditi", 8000)
fulltime = FullTimeEmployee("Rohan", 45000)
contract = ContractEmployee("Karan", 500, 80)

# Displaying salaries
intern.calculate_salary()
fulltime.calculate_salary()
contract.calculate_salary()