import random

user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()

computer_choice = random.choice(["rock", "paper", "scissors"])

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}\n")

if user_choice == computer_choice:
    print("It's a tie!")


elif user_choice == "rock" and computer_choice == "scissors":
    print("YaY!! You Win")
elif user_choice == "paper" and computer_choice == "rock":
    print("YaY!! You Win")
elif user_choice == "scissors" and computer_choice == "paper":
    print("YaY!! You Win")


elif computer_choice == "rock" and user_choice == "scissors":
    print("OOps!! Computer Wins")
elif computer_choice == "paper" and user_choice == "rock":
    print("OOps!! Computer Wins")
elif computer_choice == "scissors" and user_choice == "paper":
    print("OOps!! Computer Wins")


else:
    print("Invalid input! Please choose rock, paper, or scissors.")