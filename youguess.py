import random #Importing random

answer = random.randint(1, 10) #The answer
guess = int(input("Guess a number from 1 to 10: ")) #The guess

if guess < answer: #Uh oh, you guessed it too low!
    guess2 = int(input("Too low, try again: "))
    if guess2 < answer:
        print("You win, good job!")
    else:
        if guess2 < answer:
            guess3 = int(input("Too low, one more chance: "))
            if guess3 == answer:
                print("you win!")
            else:
                print(f"You lost! Good game. The answer was {answer}.")
        elif guess2 > answer:
            guess3 = int(input("Too high, one more chance: "))
            if guess3 == answer:
                print("you win!")
            else:
                print(f"You lost! Good game. The answer was {answer}")
        else:
            print("You win!")

        
        
elif guess > answer: #Uh oh, you guessed it too high!
    guess2 = int(input("Too high, try again: "))
    if guess2 < answer:
        guess3 = int(input("Too low, one more chance: "))
        if guess3 == answer:
            print("you win!")
        else:
            print(f"You lost! Good game. The answer was {answer}.")
    elif guess2 > answer:
        guess3 = int(input("Too high, one more chance: "))
        if guess3 == answer:
            print("you win!")
        else:
            print(f"You lost! Good game. The answer was {answer}")
    else:
        print("You win!")
else: #You win
    print("You win!")