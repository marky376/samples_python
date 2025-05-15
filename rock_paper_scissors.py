import random

options = ["rock", "paper", "scissors"]

def get_user_choice():
    while True:
        user_choice = input("Please choose one of the following: rock, paper, or scissors: ").lower().strip()
        if not user_choice:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        if user_choice in options:
            return user_choice
        print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    computer_choice = random.choice(options)
    return computer_choice
    
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif user_choice == "rock" and computer_choice == "paper":
        return "You lose!", 0, 1
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You win!", 1, 0
    elif user_choice == "paper" and computer_choice == "rock":
        return "You win!", 1, 0
    elif user_choice == "paper" and computer_choice == "scissors":
        return "You lose!", 0, 1
    elif user_choice == "scissors" and computer_choice == "rock":
        return "You lose!", 0, 1
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You win!", 1, 0

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result, user_points, computer_points = get_winner(user_choice, computer_choice)
        
        print(f"You chose {user_choice} and the computer chose {computer_choice}. {result}")
        
        user_score += user_points
        computer_score += computer_points
        print(f"Score - User: {user_score}, Computer: {computer_score}")
        
        while True:
            play_again = input("Play again? (yes/quit): ").lower().strip()
            if play_again in ["yes", "quit"]:
                break
            print("Invalid input. Please type yes or quit.")
        
        if play_again == "quit":
            print(f"Final Score - User: {user_score}, Computer: {computer_score}")
            if user_score > computer_score:
                print("You win the game!")
            elif computer_score > user_score:
                print("Computer wins the game!")
            else:
                print("It's a tie overall!")
            break

if __name__ == "__main__":
    main()