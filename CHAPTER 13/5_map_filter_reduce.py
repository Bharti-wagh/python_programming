# map() → Apply a function to every element in an iterable

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x*x, numbers))
print("Squares:", squares) 


# filter() → Keep only elements that match a condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)


# reduce() → Reduce the iterable to a single value
from functools import reduce
sum_all = reduce(lambda a, b: a + b, numbers)
print("Sum:", sum_all)