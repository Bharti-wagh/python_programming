class Employee:
    def __init__(self):
        print("Constructor of Employee")
    num1=1

class programmer(Employee):
    def __init__(self):
        print("Constructor of coder")
    num2=2

class manager(programmer):
    def __init__(self):
        super().__init__() #constructor of coder also executes 
        print("Constructor of Programmer")
    num3=3

# o=Employee()
# print(o.num1) #run successfully
# # print(o.num2) #shows error 

# o=programmer()
# print(o.num1,o.num2)

o=manager()
print(o.num1,o.num2,o.num3)
