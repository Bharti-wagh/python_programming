class student:
    subject="MATH"
    year=2019

    def __init__(self,name,subject,year): #THIS IS DUNDER METHOD WHICH IS AUTOMATICALLY CALLED
        self.name=name
        self.subject=subject
        self.year=year

        print("I AM CREATING OBJECT ")

    @staticmethod
    def getInfo(self):
        print(f"The subject IS {self.subject} THE year IS {self.year}")
        
test=student("BHARTI","MATH",2019)
test.name="BHARTI"
print(test.name,  test.subject, test.year)