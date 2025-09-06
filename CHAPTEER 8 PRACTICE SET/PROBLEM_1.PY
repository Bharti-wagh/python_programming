#WAP USING FACTORIAL TO FIND GREATEST OF THREE NUMBERS.

import math

def find_greatest_using_factorial(a, b, c):
    # Calculate factorials
    fact_a = math.factorial(a)
    fact_b = math.factorial(b)
    fact_c = math.factorial(c)

    # Compare factorials to determine greatest original number
    if fact_a >= fact_b and fact_a >= fact_c:
        return a
    elif fact_b >= fact_a and fact_b >= fact_c:
        return b
    else:
        return c

# Example usage
num1 = 4
num2 = 6
num3 = 55

greatest = find_greatest_using_factorial(num1, num2, num3)
print("Greatest number :", greatest)
