#WAP TO PRINT THE FOLLOWING STAR PATTERN
"""
***
* * #FOR N=3
***
"""

n = 3  # Size of the square

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()