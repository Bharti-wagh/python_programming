#WRITE A PYTHON FUNCTION WHICH CONVERTS INCHES TO CMS.

def inches_to_cm(inches):
    cm = inches * 2.54
    return cm

# Example usage
inches = 10
converted = inches_to_cm(inches)
print(f"{inches} inches = {converted} cm")
