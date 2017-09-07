import random

random_number = random.randint(1, 10)

def welcome():
    print("""
          Welcome to the random number generator.
          We've picked a random number between 1 and 10.
          Your job is to guess our number.
          Good luck!
          """)


def guess_number():
    while True:
        guess = int(input("Make a guess"))
        if guess == random_number:
            print("You guessed correct!")
            break
        else:
            print("Wrong guess!")
            continue


welcome()

guess_number()
