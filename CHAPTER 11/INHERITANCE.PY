class Employee:
    company="itc"
    def show(self):
        print(f"the name is {self.name}and the salary is {self.salary}")

class programmer(Employee):
    company="ItcInfotech"
    # def show(self):
    #     print(f"the name is {self.name}and the salary is {self.salary}")

    def showlanguage(self):
        print(f"the name is {self.name}and the salary is {self.language}")


a=Employee()
b=programmer()

print(a.company,b.company)