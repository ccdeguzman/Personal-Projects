"""
Personal Project: Rock Paper Scissor Game
By:  Christian De Guzman
"""
from random import randint

#score tracker
def score(player, computer, player_score, computer_score, choices):
  if player == computer:
    print("You both tied, no score")
    return player_score, computer_score
    
  if player == "s":
    if computer == "p":
      player_score += 1
      print("Scissor beats paper")
    else:
      computer_score += 1
      print("Rock Beats Scissor")
    
  elif player == "r":
    if computer == "s":
      player_score += 1
      print("Rock beats Scissor")
    else:
      computer_score += 1
      print("Paper Beats Rock")
    
  elif player == "p":
    if computer == "r":
      player_score += 1
      print("Paper Beats Rock")
    else:
      computer_score += 1
      print("Scissor Beats Rock")

  return player_score, computer_score
  
#check winner
def winner(player_score, computer_score, win_flag):
  if player_score == 2:
    print("Congratulations! You won!...")
    print("Against a computer... Go outside! touch grass!")
    win_flag = True
    return win_flag
  else:
    if computer_score == 2:
      print("You lost! How are you letting a computer beat you?! ChatGPT is already taking your job. Now you can't win a rock paper scissor game!")
      win_flag = True
      return win_flag
  
  return

if __name__ == "__main__":
  #r is for rock, s is for scissor, p is for paper
  choices = ["r", "s", "p"]
  player_score = 0
  computer_score = 0
  win_flag = False

  player = input("Enter r for 'Rock', s for 'Scissor', p for 'paper', and q to quit: ")
  computer = choices[randint(0,2)]

  while player != "q" and not win_flag:
    if player in choices:
      print("You chose,", player)
      computer = choices[randint(0,2)]
      print("The computer chooses,", computer)
      score(player, computer, player_score, computer_score, choices)
      player_score, computer_score = score(player, computer, player_score, computer_score, choices)
      print(f"Player Score: {player_score} Computer Score: {computer_score}")
      win_flag = winner(player_score, computer_score, win_flag)
      player = input("Enter r for 'Rock', s for 'Scissor', p for 'paper', and q to quit: ")
    else:
      print("Enter a valid choice")
      player = input("Enter r for 'Rock', s for 'Scissor', p for 'paper', and q to quit: ")
      
      
      
      
    
    



  
  
  