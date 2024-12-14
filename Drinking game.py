from random import randint
a=0
while a < 100:
#Storage
 names=[""]
 order=[""]
 win=[""]
 nGen= randint(0,10)
 names.remove("")
 order.remove("")
 win.remove("")
 print("Welcome to the phils drinking game, Please enter the next few information with certainty.")
 print("Please enter the amount of participants")
 t=int(input("Number: "))
 
 
 b=0
 while b<t:
  c=0
  print("Enter your names")
  nam=input("Name:")
  if nam in names:
   print("The name is already in use, please use a new name")
   continue
  else:
   names.append(nam)
   order.append(c)
   c+=1
   b+=1
   print(names)
 print("Please enter the amount of rounds you wish to do")
 t2=int(input("Num: "))
 i=0
 d=0
 while d <1000:
  if d>t2:
   print("Your rounds are over. Thank you for playing")
   print("The winners are as follows:")
   print(win)
   print("Do you wish to (1) Start over or (2) play more rounds? (3)To end the program")
   t3=int(input("Please enter your choice: "))
   if t3==1:
    print("THanks for your choice")
    break
   elif t3==2:
    print("Thanks for your choice")
    print("Please enter the amount of rounds you wish to do")
    t2=int(input("Num: "))
    d=0
    continue
   elif t3==3:
    print("Thanks for using our program")
    break
   else:break

  if i==t:
    i=0
    d+=1
    print("You have all failed.")
    print("The number is: ",nGen)
    nGen= randint(0,10)
    continue
  
  print(names[i]," Please guess a number between 0 and 10 below: ")
  t1=int(input("Num: "))
  if t1==nGen:
   print("Congrats, You have chosen the correct number")
   print("You can now ask anyone of your choice to carry out a singular task\n")
   nGen= randint(0,10)
   i+=1
   d+=1
   continue
  elif t1!=nGen:
   print("You have chosen the wrong number")
   
   print("You are now required to take a shot.\n")
   
   i+=1
   continue
  else:
   print("")
   
   

   
  
 
 a+=1
 if t3==1:
  continue
 elif t3==3:
  break

  
  