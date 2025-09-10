class Employee:
    company="itc"
    name="dummy"
    def show(self):
        print(f"the name is {self.name} and the company is {self.company}")

class coder:
    language="python"
    def printlanguage(self):
        print(f"the language is {self.language} and the language is Good")

class programmer(Employee,coder):
    company="ItcInfotech"

    def showlanguage(self):
        print(f"the name is {self.company}and the company is Good with {self.language} language")



a=Employee()
b=programmer()

b.show()
b.printlanguage()
b.showlanguage()

