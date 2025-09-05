#WAPTO PRINT FOLLOWING STAR PATTERN.
'''
    *
   ***
  *****
'''
rows = 3  # Number of rows in the pattern

for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)