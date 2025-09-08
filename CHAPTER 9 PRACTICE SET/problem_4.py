#4. A life contains a word "Donkey" multiple times.you need to write a program which replace this word with ##### by updating 
# the same life.DeprecationWarning 

word="Donkey"

with open("file.txt","r") as f:
    content=f.read()

contentNew=content.replace(word,"#####")

with open("file.txt","w") as f:
    f.write(contentNew)