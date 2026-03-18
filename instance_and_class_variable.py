class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")

employee = Employee("Dhananjay", 50000)
employeetwo = Employee("Rahul", 10000)

employee.display()  
employeetwo.display()
