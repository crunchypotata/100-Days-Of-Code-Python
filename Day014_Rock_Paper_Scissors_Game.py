print("Rock, paper, scissors game")
print()

from getpass import getpass as input

player1 = input("What's your name?")
print("Hello", player1, "!")

itemOfplayer1 = input("What item do you want to choose?: ")

player2 = input("What's your name?")
itemOfplayer2 = input("What item do you want to choose?: ")

if itemOfplayer1 == "rock" and itemOfplayer2 == "scissors":
  print("Win", player1, "!")
  
elif itemOfplayer1 == "paper" and itemOfplayer2 == "rock":
  print("Win", player1, "!")
  
elif itemOfplayer1 == "scissors" and itemOfplayer2 == "paper":
  print("Win", player1, "!")

elif itemOfplayer2 == "rock" and itemOfplayer1 == "scissors":
  print("Win", player2, "!")

elif itemOfplayer2 == "paper" and itemOfplayer1 == "rock":
  print("Win", player2, "!")

elif itemOfplayer2 == "scissors" and itemOfplayer1 == "paper":
  print("Win", player2, "!")
  
else: 
  print("Friendship won!")
