name ="bharti"
print(len(name)) # shows length of word 
################################################ Case Conversion ###################################################

text = "Hello WORLD"
print(text.lower())     # string to lowercase

text = "Hello World"
print(text.upper())     #string to uppercase.

text = "hello python world"
print(text.title())     # Capitalizes the first letter of each word, and lowers the rest.

print(name.capitalize()) #Capitalizes first letter

text = "PyTHon"
print(text.swapcase())    # Swaps the case of each character: uppercase becomes lowercase and vice versa.

############################################## Trimming ########################################################

text = "   Hello World   "
print(text.strip())  #	Removes whitespace from both ends
text = "xxPythonxx"
print(text.strip("x")) #By default, removes spaces

text = "   Hello"
print(text.lstrip()) #	Removes whitespace from the left only
text = ">>>Hello"
print(text.lstrip(">")) 

text = "Hello   "
print(text.rstrip()) #Removes whitespace from the right only
text = "Hello***"
print(text.rstrip("*")) 


##################################################Search & Find#####################################################

text = "banana"
print(text.find("a"))    #Returns the index of the first occurrence of the substring sub.If not found, returns -1 (does not raise an error).
print(text.find("z")) 

print(text.rfind("a")) #Returns the index of the last occurrence of the substring.Returns -1 if not found.

text = "banana"
print(text.index("n"))   ##Same as find(), but raises a ValueError if the substring is not found.
#print(text.index("z"))   #substring not found

print(text.rindex("n"))  #Same as rfind(), but raises an error if the substring is not found.

#################################################### Replace & Join ####################################################

words = ["2025", "07", "05"]
print("-".join(words)) #Combine strings with a separator	

words = ["I", "love", "Python"]
print(" ".join(words))

######################################################## Count ###################################################

print(name.count("a")) #Counts occurrences

######################################################## Check Types (True/False) ##################################################


#All digits
print("123".isdigit()) #True 
print("123a".isdigit())  #false


#	Letters or digits
print("123".isalnum())       # True
print("abc!".isalnum())      # False


#All whitespace
print("\n\t ".isspace())     # True
print(" a ".isspace())       # False


#	All alphabetic characters are lowercase
"hello".islower()     # True
"Hello".islower()     # False


#All alphabetic characters are uppercase
"HELLO".isupper()     # True
"HELlo".isupper()     # False


#	Title case (each word capitalized)
"Hello World".istitle()   # True
"Hello world".istitle()   # False

################################################### Split & Partition ####################################################

#Splits string by separator 
text = "Python is awesome"
print(text.split()) 

text = "apple,banana,mango"
print(text.split(",")) 

#Splits into 3 parts at first match
text = "key=value"
print(text.partition("=")) 

text = "hello"
print(text.partition(":")) 

####################################################### Starts/Ends ######################################################

print((name.endswith('i'))) # ends with i then True otherwise false
print(name.startswith('i')) # ends with i then True otherwise false

######################################################## replace ########################################################

text = "one one one"  
result = text.replace("one", "two", 1) #string.replace(old, new, count)
print(result)     # Output: two one one

text = "apple banana apple"
result = text.replace("apple", "orange")
print(result)     # Output: orange banana orange

