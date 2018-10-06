class Employee:

    employeeNum = 0

    def __init__(self, name,email, salary,roles):
        self.name = name
        self.email = email
        self.salary = salary
        self.roles = roles
        Employee.employeeNum += 1

    def displayCount(self):
       print("Number of emplyees: " % Employee.employeeNum)

    def displayEmployee(self):
        # return "{} {} earns {} per month".format(self.first, self.salary)
        print("Name = ",self.name, "Email:", self.email, " Salary:", self.salary, "Roles:", self.roles,)

class Manager(Employee):
    def __init__(self, name, email, salary, roles):
        super().__init__(name, email, salary, roles="manager")

firstEmployee = Employee("Bryan musyoki","musyokibr@gmail.com",2000, "developer")
firstEmployee.displayEmployee()

secondEMployee = Employee("Mutua Mulati","Mulatims@gmail.com",1500, "cleaner")
secondEMployee.displayEmployee()

thirdEMployee = Manager("John Cena","cenajohn@gmail.com",3000, "Manager")
thirdEMployee.displayEmployee()

print("Total Employee %d" % Employee.employeeNum)
