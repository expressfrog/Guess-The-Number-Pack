import random #Importing random

answer = int(input("Type in a number from 1 to 10: ")) #The answer
guess = random.randint(1, 10)

if answer > 10:
    print("Too high! Run this again to coninue.")
    quit()
elif answer < 1:
    print("Too low! Run this again to coninue.")
    quit()


if guess == answer:
    print("Your computer guessed you number right!")
else:
    guess2 = random.randint(1, 10)
    if guess2 == answer:
        print("You computer guessed it right!")
    else:
        guess3 = random.randint(1, 10)
        if guess3 == answer:
            print("You computer won!")
        else:
            print("You compiuter lost, Good job!")