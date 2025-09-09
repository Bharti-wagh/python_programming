#WRITE A CLASS "CALCULATOR" CAPABLE OF FINDING SQUARE , CUBE AND SQUARE ROOT OF A NUMBER.
class calculator:
    def  __init__(self,num1):
        self.num1=num1

    def square(self):
        print(f"square is {self.num1*self.num1}")

    def cube(self):
        print(f"cube is {self.num1*self.num1*self.num1}")

    def squareRoot(self):
        print(f"square root is {self.num1**1/2}")

s=calculator(2)
s.square()
s.cube()
s.squareRoot()