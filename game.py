# we need the random "library"
from random import randrange
# makes a number between 0 and 100 (excluding 100)
# and saves it into a variable called "answer"
answer = 25 #randrange(100)
# run the code inside of the while loop forever 
while True:
    # ask the player for a number and save it 
    player_guess = int(input("Guess a number: "))
    if (answer == player_guess):
        print("You win!")#print win message 
        break # end the game by breaking the loop 
    if ( player_guess < answer ):
        print("It's smaller")
    else:
        print("It's bigger")