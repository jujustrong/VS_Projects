import time
from random import randint 

def roll_dice():
    print("The dice are rolling out onto the table!")
    piece1 = randint(1,6)
    print("It looks like the first piece is a...")
    time.sleep(1)
    print(f"{piece1}!")
    time.sleep(1)
    piece2 = randint(1,6)
    print("And it looks like the second piece is a...")
    time.sleep(1)
    print(f"{piece2}!")
    total = piece1 + piece2
    time.sleep(1.5)
    
    if total == 7:
        print("Lucky number 7! You win!")
        go_again = input("Roll again? (Y or N): ")
        if go_again.upper() == "Y":
            roll_dice()
        return
    
    elif piece1==1 and piece2==1:
        print("Snake Eyes! You Win!")
        go_again = input("Roll again? (Y or N): ")
        if go_again.upper() == "Y":
            roll_dice()
        return
    
    else:
        print(f"Your total was {total}, better luck next time!")
        go_again = input("Roll again? (Y or N): ")
        if go_again.upper() == "Y":
            roll_dice()
        return
    

def dice_roller():
    print("Welcome to the Dice Roller!")
    time.sleep(1.5)
    print("We have given you 2 six-sided die")
    time.sleep(1)
    print("If you roll a 7 or Snake Eyes (two 1's) you win!")
    
    ready = input("Ready to roll? (Y or N): ")
    if ready.upper() == "N":
        return
    elif ready.upper() == "Y":
        roll_dice()
        return
    


dice_roller()
    