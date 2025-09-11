#STORE THE MULTIPLICATION TABLES GENERATED IN PROBLEM 3 IN A FILE NAMED TABLE.TXT
num = int(input("Enter a number: "))
table = [num * i for i in range(1, 11)]

with open("table.txt", "w") as f:
    for i, value in enumerate(table, start=1):
        f.write(f"{num} x {i} = {value}\n")

print("Multiplication table saved to table.txt")