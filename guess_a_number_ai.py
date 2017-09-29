import random

# config
low = 1
high = 100


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

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

    print("Think of a number between 1 and 100. Don't cheat scumbag.")
    print()
    input("Press enter to continue")
    print()
    
    
    pass

def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    print(guess)
    print("Was my guess too high, too low or correct?")
    decision = input("")

    if decision == 'high' or decision == 'h' or decision == 'High':
        return 1
    elif decision == 'low' or decision == 'l' or decision == 'Low':
        return -1
    elif decision == 'correct' or 'c':
        return 0
    else:
        print("Enter High, Low or Correct, kid.") 
        
    

    

def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    

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


