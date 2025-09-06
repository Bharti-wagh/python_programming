# Recursion is a function which call itself.
def FACTORIAL(N):
    if(N==1 or N==0):
        return 1 
    return N*FACTORIAL(N-1)


N=int(input("ENTER A NUMBER :"))
print(F"THE FACTORIAL OF THIS NUMBER IS : {FACTORIAL (N)}")




