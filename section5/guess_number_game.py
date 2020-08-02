# This is the guess the number game
import random

# Global variables
maxNumber = 20
maxGuesses = 6
playerName = ''

def main():
    global playerName
    print("Hello, What is your name?")
    playerName = input()
    secretNumber = random.randint(1, maxNumber)
    print('Well, ' + playerName +
          ' I am thinking of a random number between 0 and ' + str(maxNumber))

    # Ask the player to guess 6 times
    for guessesTaken in range(1, maxGuesses + 1):
        remainingGuesses = maxGuesses - guessesTaken
        print('Take a guess, you have ' + str(remainingGuesses) + ' remaining:')
        try:
            guess = int(input())
            if guess < secretNumber:
                print('Guess is too low!')
            elif guess > secretNumber:
                print('Guess is too high!')
            else:
                break
        except ValueError:
            print('ERROR: Input was not a valid number')
        except:
            print('ERROR: Some other error occurred..')

    if guess == secretNumber:
        print('Good job, you guessed the number in ' +
              str(guessesTaken) + ' guesses!')
    else:
        print('Bad luck the number was ' + str(secretNumber) + ' !')

main()
