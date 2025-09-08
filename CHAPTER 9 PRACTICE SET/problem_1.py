#1. Write a program to read the text from a given file 'poems.txt' and find out wheather it contains the word 'twinkle'.
f=open("poems.txt")
c=f.read()
if ("Twinkle" in c):
    print("the word Twinkle is present")
else:
    print("the word Twinkle is not present")
f.close()