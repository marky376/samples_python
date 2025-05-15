import random

options = ["rock", "paper", "scissors"]
def get_user_choice():
    while True:
        user_choice = input("Please choose one of the following: rock, paper, or scissors: ").strip().lower()
        if not user_choice:
            print("Error: Input cannot be empty. Please try again.")
        elif user_choice in options:
            return user_choice
        else:
            print("Error: Invalid choice. Please choose rock, paper, or scissors.")

# ... existing code ...

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
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = get_winner(user_choice, computer_choice)
        print(f"You chose {user_choice} and the computer chose {computer_choice}. {result}")
        
        # Update scores based on result
        if "win" in result.lower():
            user_score += 1
        elif "lose" in result.lower():
            computer_score += 1
            
        # Display current score
        print(f"Score - User: {user_score}, Computer: {computer_score}")
        
        # Ask to play again
        play_again = input("Play again? (yes/quit): ").strip().lower()
        if play_again != 'yes':
            # Display final summary
            print("\nGame Over!")
            print(f"Final Score - User: {user_score}, Computer: {computer_score}")
            if user_score > computer_score:
                print("Congratulations! You are the overall winner!")
            elif computer_score > user_score:
                print("Sorry, the computer is the overall winner.")
            else:
                print("It's a tie overall!")
            break

if __name__ == "__main__":
    main()