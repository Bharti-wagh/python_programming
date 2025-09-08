#WRITE A PYTHON FUNCTION TO PRINT FIRST N LINES OF THE FOLLOWING PATTERN:

'''
***
**    -FOR N=3
*
'''

def print_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

# Example usage
print_pattern(3)