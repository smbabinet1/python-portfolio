#Scarlett
#1/7/25
#Rock Paper Scissors

#Init
import random
#Functions
def rpsgame():
    print("Welcome to Rock Paper Scissors!")
    while True:
        print("What is your move?")
        player = str(input("Rock, Paper, Scissors, Shoot: "))
        player = player.lower()
        #Step 2: generate computer's move
        computer = random.randint(1,3)
        if computer == 1:
            computer = "rock"
            print("The computer's move is Rock!")
        elif computer == 2:
            computer = "paper"
            print("The computer's move is Paper!")
        elif computer == 3:
            computer = "scissors"
            print("The computer's move is Scissors!")
    #Step 3: compare scores
        if computer == player:
            print("It's a tie!")
        elif computer == "rock" and player == "paper":
            print("You win!")
        elif computer == "rock" and player == "scissors":
            print("You lose!")
        elif computer == "paper" and player == "rock":
            print("You lose!")
        elif computer == "rock" and player == "scissors":
            print("You lose!")
        elif computer == "scissors" and player == "rock":
            print("You win!")
        elif computer == "scissors" and player == "paper":
            print("You lose!")
        x = input("Would you like to continue playing?")
        x = x.lower()
        if x == "no":
            break
#Main

rpsgame()

