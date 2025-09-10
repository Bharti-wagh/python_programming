class Employee:
    num1=1

class programmer(Employee):
    num2=2

class manager(programmer):
    num3=3

o=Employee()
print(o.num1) #run successfully
# print(o.num2) #shows error 

o=programmer()
print(o.num1,o.num2)

o=manager()
print(o.num1,o.num2,o.num3)