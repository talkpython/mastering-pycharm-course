import random

print("Welcome to the HI - LO game")
true_number = random.randint(1, 100)
while True:
    guessed_number = int(input("Guess a number between 1 & 100: "))
    if guessed_number == true_number:
        print("Got it: {true_number}".format(true_number=true_number))
        break
    elif guessed_number < true_number:
        print("Too low!")
    else:
        print("Too high!")
