import random

secretNumber = random.randint(1, 100)
win = False

while not win:
    print("Guess a number.")
    guess = int(input())
    if guess == secretNumber:
        print("You got it right!")
        win = True
    else:
        if guess > secretNumber:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
