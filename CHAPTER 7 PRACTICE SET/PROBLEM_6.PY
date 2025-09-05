#WAP TO CALCULATE THE FACTORIAL OF A GIVEN NUMBER USING FOR LOOP.
#5!=1 x 2 x 3 x 4 x 5 
n=int(input("enter number : "))
p=1
for i in range (1,n+1):
    p=p*i
print(f"The factorial of {n} IS {p}")