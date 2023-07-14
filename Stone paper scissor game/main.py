# .......... STONE PAPER SCISSSORS ...........
import random

def game(comp,your):
    if comp==your:
        return None
    
    if comp=='r':
        if your == 's':
            return False
        elif your == 'p':
            return True

    if comp=='p':
        if your == 'r':
            return False
        elif your == 's':
            return True

    if comp=='s':
        if your == 'p':
            return False
        elif your == 'r':
            return True
            
print("Computer's Turn : Rock(r) , Paper(p) , Scissors(s) ")
randChoice = random.randint(1,3)
if randChoice==1:
    comp='r'
elif randChoice==2:
    comp='p'
elif randChoice==3:
    comp='s'

your = input("Your turn : Rock(r) , Paper(p) , Scissors(s) ")

print(f"Computer Chose {comp}")
print(f"You Chose {your}")

res = game(comp, your)

if res==None:
    print("The Game is Tied!")
elif res:
    print("You Won!")
else:
    print("You Lose!")


