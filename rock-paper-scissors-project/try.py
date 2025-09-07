import random
print("rock-paper-scissors game")
print("1.Rock\n2.paper\n3.scissors")
choice=int(input("Enter your choise from 1 to 3 : "))
if choice>3:
  print("Invalid choice")
schoice=random.randrange(1,3)
print(f"System choice : {schoice}")
if choice==1 and schoice==3:
  print("Uh win!!!")
elif choice==3 and schoice==2:
  print("uh win!!")
elif choice==2 and schoice==1:
  print("uh win!!!")
elif choice==schoice or choice==0:
  print("ohh it's tie ")
else:
  print("Uh loss,try next time")


