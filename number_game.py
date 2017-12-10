import random

def game():
    # generate a random number between 1 and 10
    secret_number = random.randint(1,10)
    guesses = []
    #Count
    count = 0
    #Create a game loop
    while len(guesses) < 5:
        count = count + 1
        try:
            # get a number guess from a player
            # guess = int(input("Guess a number between 1 and 10: "))
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("Please guess a number!")
        else:
            # compare guess to secret number
            if guess == secret_number :
                print("Congrats you got it after {} try!".format(secret_number))
            elif guess < secret_number:
                print("my number is higher than {}!".format(guess))
            else guess > secret_number:
                print("my number is lower than {}!".format(guess))
            guesses.append(guess)
    #after the the while loop is complete it'll print below
    else:
        print("Too many tries! The number was {}! Game over!".format(secret_number))
    play_again = input("Do you want to play again? Y/n")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")
game()
