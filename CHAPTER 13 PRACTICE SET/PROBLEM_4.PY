#WAP TO FING THE MAXIMUM OF THE NUMBERS IN A LIST USING REDUCE FUNCTION.
from functools import reduce
numbers = [10, 25, 7, 89, 45, 67]
max_num = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum number:", max_num)
