#5. Repeat program 4 for a list of to be ceensored.

words=["Donkey","bad","fine"]

with open("file.txt","r") as f:
    content=f.read()

for word in words:
    content=content.replace(word,"#" *len(word))

with open("file.txt","w") as f:
    f.write(content)