import random

options = ["rock", "paper", "scissors"]

def get_user_choice():
    while True:
        user_choice = input("Please choose one of the following: rock, paper, or scissors: ").strip().lower()
        if not user_choice:
            print("Input cannot be empty. Please try again.")
            continue
        if user_choice in options:
            return user_choice
        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(options)

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
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = get_winner(user_choice, computer_choice)
        print(f"You chose {user_choice} and the computer chose {computer_choice}. {result}")

        if "You win" in result:
            user_score += 1
        elif "You lose" in result:
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        while True:
            play_again = input("Play again? (yes/quit): ").lower().strip()
            if play_again in ["yes", "quit"]:
                break
            print("Please enter 'yes' or 'quit'.")

        if play_again == "quit":
            print(f"\nFinal score - You: {user_score}, Computer: {computer_score}")
            if user_score > computer_score:
                print("Congratulations! You are the overall winner!")
            elif computer_score > user_score:
                print("The computer is the overall winner...")
            else:
                print("The game ended in a tie!")
            break

if __name__ == "__main__":
    main()