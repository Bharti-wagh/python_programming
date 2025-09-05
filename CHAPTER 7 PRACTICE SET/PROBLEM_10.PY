#WAP TO PRINT MULTIPLICATION TABLE OF N USING FOR LOOPS IN REVERSAL ORDER.
n = int(input("Enter a number: "))

for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")