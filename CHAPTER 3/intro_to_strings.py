#string is immutable (not changable)
name='bharti' #single quote string
dname="bharti" # doublee cote string
nname="""bharti""" #triple quote string

print(name)
print(dname)
print(nname)

print(name[2:6])

print(name[0:5])

print(name[:5]) #by default starts from 0 string 

print(name[0:]) #empty space is a length 




# start = 1 → starts at index 1 ('m')

# stop = 6 → goes up to but not including index 6 ('n')

# step = 2 → takes every 2nd character
Word = 'amazing'
print(Word[1:6:2]) #step = 2 → takes every 2nd character 