#HOW DO YOU PREVENT A PYTHON PRINT() FUNCTION TO PRINT A NEW LINE AT END.
'''
In Python, the print() function adds a newline (\n) at the end by default.

To prevent it from printing a new line at the end, use the end parameter like this:
'''

print("Hello", end="")  # No newline after this print

#EXAMPLE
print("Hello", end="")
print("World")

#You can also use a space or any custom separator:
print("Hello", end=" ")
print("World")