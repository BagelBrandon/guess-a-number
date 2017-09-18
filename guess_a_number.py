import random

# config
low = 1
high = 100

#Helper Functions
def get_guess():
    while True:
        guess = input("Guess a number:")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def play_again():
    while True:
        decision = input("You wanna have another go?")

        if decision == 'yes' or decision == 'y' or decision == 'Yes':
            return True
        elif decision == 'no' or decision == 'No' or decision == 'n':
            return False
        else:
            print ("Use yes or no you imbecile")

again = True

while again:        
#start game
    rand = random.randint(low, high)
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

    guess = -1
    tries = 0
    limit = 10

    #play game
    while guess != rand and tries < limit:
        guess = get_guess()
        
        if guess < rand:
            print("You guessed too low.")
        elif guess > rand:
            print("You guessed too high.")
            
        tries +=1

    # end
    if guess == rand:
        print("Good job kid, you know basic math")
    else:
        print ("You're trash at everything, loser. The number was " + str(rand) + ".")

    again = play_again()


print("Peace nerd")
