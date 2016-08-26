from random import randint
from time import sleep

options =["R","P","S"]

LOSS_MESSAGE = "You lost!"
WIN_MESSAGE = "You won!"

#Compare user_choice and computer_choice to figure out the winner!

def decide_winner(user_choice, computer_choice):
  print "User choice: %s \n Computer selecting..." % user_choice
  sleep(1)
  print "Computer's choice: %s" % computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print "It's a tie!"
  elif (user_choice_index == 0 and computer_choice_index == 2) or (user_choice_index == 1 and computer_choice_index == 0) or (user_choice_index == 2 and computer_choice_index == 1):
    print WIN_MESSAGE
  elif user_choice_index > 2:
    print "Invalid choice!"
    return
  else:
    print LOSS_MESSAGE
    
#Ask the user for choice of R, P or S:
def play_RPS():
  print "ROCK PAPER SCISSORS:"
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors:")
  user_choice = user_choice.upper()
  sleep(1)
  if user_choice in options:
  	computer_choice  = options[randint(0,len(options)-1)]
  	decide_winner(user_choice, computer_choice)
  else:
    print "Invalid choice!"
  
play_RPS()
