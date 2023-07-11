#a=int(input("Enter the number that you want to guess\n"))
import random
a=random.randrange(1,100)
b=9
for x in range(9):

    c=int(input("Enter the number\n"))
    b=b-1
    if c>a:
        print("The Number is grater than target\n")
        print(b,"chances left")
        d=c
        continue
    elif c<a:
        print("The number is less than target number\n")
        print(b,"chances left")
        d=c


        continue
    else:
        print("Congratulation you have Entered target number")
        break
print("Game Over!\n")
if c==a:
    print("You Entered right Number")
else:
    print("Better Luck Next Time")

