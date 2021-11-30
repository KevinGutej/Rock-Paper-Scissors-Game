import random

def play():
    user = input("What's Your choice? 'r' for rock, 'p' for paper, 's' for scissors\n") #user choices
    computer = random.choice(['r', 'p', 's']) # computer random choices

    if user == computer: # If user and computer get the same choice
        return 'It\'s a tie' # prints out 'tie'

    if is_win(user, computer): #If our choice wins the computer
        return 'You Won!' #prints out 'You Won!'

    return 'You Lost!' #No need for a else as if the other 2 cases do not work then there is only one thing left to do.


def is_win(player, opponent): # Checking what we and the computer have inputed and all the possible sequences
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())