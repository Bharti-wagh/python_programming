# Write __str__() method to print the vector as follows 7i+8j+10k:

class Vector:
    def __init__(self, components):
        self.components = list(components)

    def __str__(self):
        basis = ['i', 'j', 'k'] + [f'e{n}' for n in range(4, len(self.components) + 1)]
        terms = []
        for coeff, unit in zip(self.components, basis):
            if coeff != 0:  
                terms.append(f"{coeff}{unit}")
        return "+".join(terms)

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension to add")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for dot product")
        return sum(a * b for a, b in zip(self.components, other.components))

v1 = Vector([7, 8, 10])
v2 = Vector([1, 2, 3])

print("v1 =", v1)        # 7i+8j+10k
print("v2 =", v2)        # 1i+2j+3k
print("Addition =", v1 + v2)  # 8i+10j+13k
print("Dot Product =", v1 * v2)  # 53

