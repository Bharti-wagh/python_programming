# WAP TO FILTER A LIST OF NUMBERS WHICH ARE DIVISIBLE BY 5.
numbers = [10, 23, 45, 66, 75, 82, 90]

divisible_by_5 = list(filter(lambda x: x % 5 == 0, numbers))

print("Numbers divisible by 5:", divisible_by_5)
