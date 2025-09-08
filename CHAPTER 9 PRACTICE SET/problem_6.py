#6. WAP to mine a log file and find out wheatheer it contains 'python'.
with open("log.txt") as f:
    content=f.read()

if ("python" in content):
    print("python is present")
else:
    print("python is not present")