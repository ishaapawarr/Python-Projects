class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # Corrected 'salaray' to 'salary'

    def getSalary(self):
        print(self.salary)

rohan = Employee("Rohan", "45000")
#print(rohan.salary)
#print(rohan.name)
rohan.getSalary()

isha = Employee("Isha", "60000")
#print(isha.salary)
#print(isha.name)
isha.getSalary()