#CREATE A CLASS WITH A CLASS ATTRIBUTE A; CREATE AN OBJECT FROM IT AND SET 'A' DIRECTLY USING 
# OBJECT.A=O.   DOES THIS CHANGE THE CLASS ATTRIBUTE ?
class demo:
    A=4

o=demo()
print(o.A) #print instance attribute
o.A=0 #instance attributes
print(o.A) #print instance attribute 
print(demo.A) #print the class attribute
