# WAP TO DISPLAY A/B WHEERE A AND B ARE INTEGERS. IF B=0 , DISPLAY INFINITE BY HANDLING THE "ZERODIVISIONERROR".
try:
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Infinite (division by zero not possible)")
