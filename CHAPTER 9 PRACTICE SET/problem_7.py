#7. WAP to find out the line number where python is present from ques 6.
with open("log.txt")as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("python"in line):
        print(f"yes python is present line no:{lineno}")
        break
    lineno +=1

else:
    print("python is not present")