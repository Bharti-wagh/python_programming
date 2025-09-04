"""
WAP TO CALCULATE THE GRADE OF STUDENT FROM HIS MARKS FROM THE FOLLOWING SCHEME.
90-100 =>EX
80-90 =>A
70-80 =>B
60-70 =>C
50-60 =>D
<50 =>F
"""

Marks=int(input("Enter here marks obtained : "))
if (Marks<50):
    print(" F ")
elif (Marks<=60 and Marks>=50):
    print(" D ")
elif (Marks<=70 and Marks>=60):
    print(" C ")
elif (Marks<=80 and Marks>=70):
    print(" B ")
elif (Marks<=90 and Marks>=80):
    print(" A ")
elif (Marks<=100 and Marks>=90):
    print(" EX ")
else:
    print("INVALID INPUT")

