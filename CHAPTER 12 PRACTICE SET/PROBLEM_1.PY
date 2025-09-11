# WAP TO OPEN THREE FILES 1.TXT, 2.TXT, 3.TXT IF ANY THESE FILES ARE NOT PRESENT, A MESSAGE WITHOUT EXISTING THE PROGRAM MUST BE PRINTED
# PROMTING THE SAME.

try:
    with open ("1.TXT","r") as o:
        print(o.read())

except Exception as e:
    print(e)

    
try:
    with open ("2.TXT","r") as o:
        print(o.read())

except Exception as e:
    print(e)



try:
    with open ("3.TXT","r") as o:
        print(o.read())

except Exception as e:
    print(e)