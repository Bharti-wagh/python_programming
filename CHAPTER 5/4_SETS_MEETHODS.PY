S1={1,2,3,"AISHWARYA",4,5,3,"ABHISHEK",21,12}
print(S1,type(S1))

S1.add(120)
print(S1,type(S1))

#################################################### OPERATIONS SET ########################################################################
print(len(S1))

S1.remove(2)
print(S1)

S1.pop() #random 1 element pop
print(S1)

S1.clear()
print(S1)

set1={1,2,4,5,6,2}
set2={43,5,6,87,63,45,2}
print(set1)
print(set2)

print(set1.union(set2)) #returns both sets item except repeated
print(set1.intersection(set2)) #returns that contains both sets

print(set1.difference(set2)) #Returns elements in set1 but not in set2.
print(set1.symmetric_difference(set2)) #Returns elements in set1 or set2 but not in both.
print(set1.issubset(set2)) #Checks if all elements of set1 are in set2
print(set1.issuperset(set2)) #Checks if set1 contains all elements of set2.
print(set1.isdisjoint(set2)) #Returns True if sets have no common elements.
