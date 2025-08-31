###################################### TUPLE METHODS ##################################
tuple1=(1,2,3)
tuple2=(4,5,6)
print(tuple1)
print(tuple2)

print(tuple1[2])







#################################### TUPLES OPERATION ############################################
tuple1=(1,2,3)
tuple2=(4,5,6)
print(tuple1)
print(tuple2)
concatenated =(tuple1+tuple2) #tuple concatenation using the + operator 
print(concatenated)

tuple1=(1,2,3)
reapeated=tuple1*3 #TUPLE CA REPEATED USING * OPERATOR
print(reapeated)

tuple1=(1,2,3)
print(2 in tuple1) #CHECKS THE ITEM EXIST IN TUPLE USING 'in' OPERATOR
print(4 in tuple1) #ELEMENT EXIST OUTPUT :TRUE OTHERWISE FALSE

tuple1=(1,2,3)
print(len(tuple1)) #LENGTH OF TUPLE

tuple1=(1,2,3)
# GET SMALLEST AND LARGEST ELEMENT IN A TUPLE
print(min(tuple1))
print(max(tuple1))