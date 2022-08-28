from random import *


while True:
    'loop for the player to continually choose R,P or S'
    print('Welcome to this game.')
    print("Type R, P or S for Rock, Paper, Scissors respectively\nType 'quit' to end game.")
    
    myself= 's'
    
    list = ['R', 'P', 'S']  #List that contains every choice the computer can make.

    win_dictionary = {
        'R' : 'S',
        'P' : 'R',
        'S' : 'P'
    } #A dictionary to loop to know the winner i.e. R wins S, P wins R...

    if myself.lower() == 'quit':
        print("You've ended the game.")
        break
    
    if myself.upper() == 'R':
        #If the player chooses Rock
        computer = choice(list)
        print(computer)
        break
    
    elif myself.upper() == 'P':
        #If the player chooses paper
        computer = choice(list)
        print(computer)
        break

    elif myself.upper() == 'S':
        #if the player chooses Scissors
        computer = choice(list)
        print(computer)
        break
    
    else:  
        print("\nError. Please type either 'R', 'P' or 'S'")
        break


    sys_score = 0
    your_score = 0

    if myself.upper() == computer:
        print('It is a tie')
        #sys_score +=0
        #your_score+= 0

    