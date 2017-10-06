import random
import math

# config

print("What's your name?")
name = input()
print()
print("We're gonna play a game, " + name + " pick a low Number.")
low = input()
low = int(low)

print("Now pick a high value, this number has to be larger than the low.")
high = input()
high = int(high)

limit = math.ceil(math.log(high-low + 1, 2))
tries = 0

# helper functions
def show_start_screen():
    print("""
 _____                               _   _                 _               
|  __ \                             | \ | |               | |              
| |  \/_   _  ___  ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__,_| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|   
                                                                         """)

    
def show_credits():
    print("This game was made by ya boy, BagelBrandon")
    
    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    guess = (current_low + current_high) // 2
    
    return guess


def pick_number():

    print()
    print("Think of a number between the low and high you've chosen, " + name + ". Don't cheat.")
    print()
    input("Press enter to continue")
    print("")
    
    
    pass

def check_guess(guess, tries):
    
    
    print(guess)
    print("Was my guess too high, too low or correct " + name + "?")
    decision = input()

    print()
    decision = decision.lower()
    if decision == 'high' or decision == 'h':
        return 1
    elif decision == 'low' or decision == 'l':
        return -1
    elif decision == 'correct' or decision == 'c':
        return 0
    else:
        print("Enter High, Low or Correct, " + name + ".") 
        
    

    

def show_result(guess, tries):

    print("I won, you're trash, " + name + ". It took me " + str(tries) + "tries.")
    print("""
 ___          .__         
|   | __  _  _|__| ____   
|   | \ \/ \/ /  |/    \  
|   |  \     /|  |   |  \ 
|___|   \/\_/ |__|___|  / 
                      \/
                    """)
def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Enter 'y' or 'n' please.")

def play():
    current_low = low
    current_high = high
    check = -1
    tries = 0
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess, tries)

        if check == -1:
            # adjust current_low
            current_low = low + guess
        elif check == 1:
            # adjust current_high
            current_high = high - guess

        tries += 1
    show_result(guess, tries)

    

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()


