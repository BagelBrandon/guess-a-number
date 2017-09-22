import random
import math

# config
low = 1
high = 100
limit = math.ceil(math.log(high-low + 1, 2))

# helper functions
def show_start_screen():
    print("""
 _____                              _   _                 _               
|  __ \                            | \ | |               | |              
| |  \/_   _  ___ ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ / __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ | '__|
| |_\ | |_| |  __\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __| |   
 \____/\__,_|\___|___|___/  \__,_| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|""")


def show_credits():
    print("This awesome game was created by Bagel Brandon.")
    print("")

    
def get_guess():
    while True:
        guess = input("Guess a number: ")
        print("")


        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")
            print("")


def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +". You have " + str(limit) + " turns to guess correctly.")
    print("")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
        print("")
    elif guess > rand:
        print("You guessed too high.")
        print("")

def show_result(guess, rand):
    if guess == rand:
        print("You win!")
    else:
        print("You are such a loser! The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        print("")

        if decision == 'y' or decision == 'yes' or decision == 'Yes' or decision == 'YES':
            return True
        elif decision == 'n' or decision == 'no'or decision == 'No' or decision == 'NO':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
            print("")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()

