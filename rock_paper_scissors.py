import random

options = ["rock", "paper", "scissors"]
def get_user_choice():
    user_choice = input("Please choose one of the following: rock, paper, or scissors: ")
    if user_choice in options:
        return user_choice
    else:
        print("Please choose one of the following: rock, paper, or scissors: ")
        return get_user_choice()

def get_computer_choice():
    computer_choice = random.choice(options)
    return computer_choice
    
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "paper":
        return "You lose!"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You win!"
    elif user_choice == "paper" and computer_choice == "rock":
        return "You win!"
    elif user_choice == "paper" and computer_choice == "scissors":
        return "You lose!"
    elif user_choice == "scissors" and computer_choice == "rock":
        return "You lose!"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You win!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = get_winner(user_choice, computer_choice)
    print(f"You chose {user_choice} and the computer chose {computer_choice}. {winner}")

main()    
