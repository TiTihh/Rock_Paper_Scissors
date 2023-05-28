import random


def get_choices():
    player_choice = input("get your weapon (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choices(options)
    choisis = {"player": player_choice, "computer": computer_choice}
    return choisis


def check_win(player, computer):
    print(f"You chose {player} computer chose {computer}")
    if player == "rock":
        if computer == "rock":
            return "It's a tie."
    elif player == "paper":
        if computer == "paper":
            return "It's a tie."
    elif player == "scissors":
        if computer == "scissors":
            return "It's a tie."
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win"
        else:
            return "Papers covers rock! You lose"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win"
        else:
            return "Scissor cuts paper! You lose"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win"
        else:
            return "Rock smashes scissors! You lose."


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

# here is a random error, if you fix it please send me the code fixed!
