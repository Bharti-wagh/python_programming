#CREATE CLASS "PROGRAMMER" FOR STORING INFORMATION OF FEW PROGRAMMERS WORKING AT MICROSOFT.
class PROGRAMMER:
    company="Microsoft"
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role

p=PROGRAMMER("BHARTI",22,"DEVELOPER")
print(p.name,p.age,p.role)
A=PROGRAMMER("ADITI",22,"DEVELOPER")
print(A.name,A.age,A.role)