import random

# config


print("What's your name?")
name = input()
print()
print("We're gonna play a game, " + name + " pick a low Number.")
low = input()
print("Now pick a high value, this number has to be larger than the low.")
high = input()

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
    print("This was made by ya boy Bagel Brandon")
    print("")
    
    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    guess = (current_low + current_high) // 2
    
    return guess


def pick_number():

    print()
    print("Think of a number between " + low + " and " + high + "," + name + ". Don't cheat.")
    print()
    input("Press enter to continue")
    print("")
    
    
    pass

def check_guess(guess):
    
    
    print(guess)
    decision = input("Was my guess too high, too low or correct " + name + "?")

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
        
    

    

def show_result(guess):

    print("I won, you're trash, " + name + ".")
    
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
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            # adjust current_low
            current_low = low + guess
        elif check == 1:
            # adjust current_high
            current_high = high - guess

    show_result(guess,)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()


