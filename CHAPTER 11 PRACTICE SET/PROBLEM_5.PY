#write a class vector representing a vector of n dimensions.overload the + and * operator which calculates
# the sum and the dot(.) product of them.

class Vector:
    def __init__(self, components):
        self.components = list(components)

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    # Overload '+' 
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension to add")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    # Overload '*' 
    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for dot product")
        return sum(a * b for a, b in zip(self.components, other.components))

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("v1:", v1)
print("v2:", v2)

v3 = v1 + v2
print("Addition:", v3)

dot_product = v1 * v2
print("Dot Product:", dot_product)
