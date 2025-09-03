DATA={
    "SARVADNYS":45,
    "ADITYA":67,
    "JEET":78

}
print(DATA.items()) #list of (key-value) tuples
print(DATA.keys()) #returns the dictionary keys
print(DATA.values()) #returns the dictionary values
DATA.update({"sarvadnya": 89,"om": 99})
print(DATA) #updated data print key-values
print(DATA.get("ADITYA")) #RETURN VALUES OF MENTINED KEY

print(DATA.get("ADITYA")) #IF BUT KEY NOT MATCH THEN THE OUTPUT WILL BE NONE 
print(DATA["ADITYA"]) #IF BUT KEY NOT MATCH THEN THE OUTPUT WILL BE ERROR

new_dic=DATA.copy()
print(new_dic)

DATA.pop("ADITYA") #Removes the specified key and returns its value.
print(DATA)

DATA.popitem() #Removes the last inserted key-value pair.
print(DATA)

KEYS=['A','B','C']
MY_DIC=dict.fromkeys(KEYS,0) #Creates a new dictionary from a list of keys with the same value.
print(KEYS)

DATA.CLEAR()
print(DATA)