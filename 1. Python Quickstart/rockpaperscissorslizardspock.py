from random import choice
user_action = input("Enter an action: ")

actions = ["rock", "paper", "scissors", "lizard", "spock"]
computer_action = choice(actions)
print("Computer chose: " + computer_action)

beats = {
    "rock": {"scissors", "lizard"},
    "paper": {"rock", "spock"},
    "scissors": {"paper", "lizard"},
    "lizard": {"paper", "spock"},
    "spock": {"scissors", "rock"}
}

if user_action == computer_action:
    print("Draw. Try again.")
elif computer_action in beats[user_action]: 
    print("You win!") 
else:
    print("You suck and lose.")