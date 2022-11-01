from random import random

from random import choice

#test
user_action = input("Rock, paper, scissors? ")

actions = ["rock", "paper", "scissors"]
computer_action = random.choice(actions)

if user_action == "rock" and computer_action == "rock":
    print("Draw. Play again.")
if user_action == "rock" and computer_action == "paper":
    print("You lose.")
if user_action == "rock" and computer_action == "scissors":
    print("You win.")
#...

if user_action == "rock":
    if computer_action == "rock":
        print("Draw. Play again")
    elif computer_action == "paper":
        print("You lose.")
    elif computer_action == "scissors":
        print("You win.")
elif user_action == "paper":
    if computer_action == "rock":
        print("You win.")
#...

if user_action == computer_action: 
    print("Draw. Play again.")

elif user_action == "rock":
    if computer_action == "paper":
        print("You lose.")
    elif computer_action == "scissors":
        print("You win.")
#...

# Homework (not mandatory)
# Rock, paper, scissors, lizard, spock
# https://www.youtube.com/watch?v=x5Q6-wMx-K8