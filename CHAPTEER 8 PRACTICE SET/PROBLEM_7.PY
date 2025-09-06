#WRITE A PYTHON FUNCTION TO REMOVE A GIVEN WORD FROM A LIST AND STRIP IT AT THE SAME TIME. 

def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
    
l=["bharti","bhakti","bhargavi","bhumi"]
print(rem(l,"i"))