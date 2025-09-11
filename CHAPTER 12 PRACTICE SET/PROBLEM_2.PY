#WAP TO PRINT THIRD ,FIFTH AND SEVENTH ELEMENT FROM A LIST USING ENUMERATE FUNCTION.
list1=["Bharti",1,2,"Bhakti",4,2,3,"Bhuvna"]

for i, item in enumerate (list1):
    if i==2 or i==4 or i==6:
        print(item)