class Employee:
    company = "Google"

    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")

employee = Employee("Dhananjay", 50000)
employee.display()

Employee.change_company("Microsoft")
employee.display()