import random
def get_choices():
  players_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock","paper" , "scissors"]
  computer_choices = random.choices(options)
  choices = {"player": players_choice, "computer": computer_choices}
  return choices

def check_win(player, computer):
  if(player == computer):
    return "Its a Tie"

  
  elif(player == "rock"):
    if(computer == "scissors"):
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."

  elif(player == "paper"):
    if(computer == "rock"):
      return "scissors smashes paper! You lose!"
    else:
      return "paper covers rock! You win."


  elif(player == "scissors"):
    if(computer == "paper"):
      return "scissors smashes paper! you win!"
    else:
      return "Paper covers rock! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
