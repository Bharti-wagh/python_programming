# A LIST CONTAIN MULTIPLICATION TABLE OF 7.WAP TO CONVERT IT TO VERTICAL STRING OF SAME NUMBERS.
# Multiplication table of 7 in a list
table = [7 * i for i in range(1, 11)]

# Convert to vertical string (one number per line)
vertical = "\n".join(map(str, table))

print(vertical)
