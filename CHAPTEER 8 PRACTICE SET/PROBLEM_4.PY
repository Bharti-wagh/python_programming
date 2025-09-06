#WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS.
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
print(sum(4))