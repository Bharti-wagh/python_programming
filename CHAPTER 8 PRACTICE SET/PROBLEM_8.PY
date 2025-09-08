#WRITE A PYTHON FUNCTION TO PRINT MULTIPLICATION TABLE OF A GIVEN NUMBER.
def print_table(n):
    print(f"Multiplication Table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Example usage
print_table(5)
