# ADD A STATIC METHOD IN PROBLEM 2, TO GREET THE USER WITH HELLO
class calculator:
    def  __init__(self,num1):
        self.num1=num1

    def square(self):
        print(f"square is {self.num1*self.num1}")

    def cube(self):
        print(f"cube is {self.num1*self.num1*self.num1}")

    def squareRoot(self):
        print(f"square root is {self.num1**1/2}")
        
    @staticmethod
    def greet():
        print("Hello")

s=calculator(2)
s.greet()
s.square()
s.cube()
s.squareRoot()