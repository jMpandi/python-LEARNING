import random

guess=random.randrange(1,10)
n=int(input("Enter Your no:"))

while guess!= n:
 
    if n<guess:
        print("Too low")
        n=int(input("Enter again"))
    elif n>guess:
        print("Too high")
        n=int(input("Enter again"))
    else:
      break
print("You guessed it Right")    
   