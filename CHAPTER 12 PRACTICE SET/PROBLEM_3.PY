# WRITE A LIST COMPREHENSION TO PRINT A LIST WHICH CONTAINS A MULTIPLICATION TABLE OF A USER ENTERED NUMBER.
num = int(input("Enter a number: "))
table = [num * i for i in range(1, 11)]
print(table)