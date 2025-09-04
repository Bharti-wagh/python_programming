#WAP TO FIND GREATEST OF FOUR NUMBERS ENTERED BY THE USER
NUMBER1=int(input("Enter the number 1: "))
NUMBER2=int(input("Enter the number 2: "))
NUMBER3=int(input("Enter the number 3: "))
NUMBER4=int(input("Enter the number 4: "))

if (NUMBER1>NUMBER2 and NUMBER1>NUMBER3 and NUMBER1>NUMBER4):
    print("NUMBER 1 IS GREATER")
elif (NUMBER2>NUMBER3 and NUMBER2>NUMBER4 and NUMBER2>NUMBER1):
    print("NUMBER 2 IS GREATER")
elif (NUMBER3>NUMBER2 and NUMBER3>NUMBER1 and NUMBER3>NUMBER3):
    print("NUMBER 3 IS GREATER")
elif (NUMBER4>NUMBER1 and NUMBER4>NUMBER2 and NUMBER4>NUMBER3):
    print("NUMBER 4 IS GREATER")
else:
    print("NUMBER IS NOT FOUND")
