import random


def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Choose your weapon (rock, paper, scissors): ")

    # Validar a escolha do jogador
    while player_choice not in options:
        print("Invalid choice. Please choose again.")
        player_choice = input("Choose your weapon (rock, paper, scissors): ")

    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player}, and the computer chose {computer}.")

    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."


while True:
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break


