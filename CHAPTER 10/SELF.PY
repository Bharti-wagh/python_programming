class student:
    subject="MATH"
    year=2019

    def getInfo(self):
        print(f"The subject IS {self.subject} THE year IS {self.year}")
        
    @staticmethod
    def greet():
        print("Good morning")

test=student()
test.getInfo()
test.greet()