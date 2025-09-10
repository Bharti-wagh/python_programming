#write a class 'complex' to represent complex number , along with overloaded operator '+' and '*'
#which adds and multiplies them.
class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"

    # Overloading '+' 
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # Overloading '*' 
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)


c1 = Complex(3, 2)
c2 = Complex(1, 7)

print("First complex number:", c1)
print("Second complex number:", c2)

# Addition
c3 = c1 + c2
print("Addition:", c3)

# Multiplication
c4 = c1 * c2
print("Multiplication:", c4)
