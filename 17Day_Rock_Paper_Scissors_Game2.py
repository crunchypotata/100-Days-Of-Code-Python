print("Rock, paper, scissors game")
print()

#from getpass import getpass as input

rounds = 0
p1score = 0
p2score = 0


player1 = input("What's your name?")
print("Hello", player1, "!")
print()

player2 = input("What's your name?")
print("Hello", player2, "!")
print()


while True :
  
  item_player1 = input("So, first gamer, what item do you want to choose? ")
  print()
  item_player2 = input("And you, what item do you want to choose? ")
  

  if item_player1 == "rock" and item_player2 == "scissors":
   print("Win", player1, "!")
   p1score += 1
   
    
  elif item_player1 == "paper" and item_player2 == "rock":
   print("Win", player1, "!")
   p1score += 1
   
    
  elif item_player1 == "scissors" and item_player2 == "paper":
   print("Win", player1, "!")
   p1score += 1
   
    
  elif item_player2 == "rock" and item_player1 == "scissors":
   print("Win", player2, "!")
   p2score += 1
   
    
  elif item_player2 == "paper" and item_player1 == "rock":
   print("Win", player2, "!")
   p2score += 1
   
    
  elif item_player2 == "scissors" and item_player1 == "paper":
   print("Win", player2, "!")
   p2score += 1
    
  else:
   print("Sorry, try one more time!")
    
  rounds += 1
    
  if p1score == 3:
   print("Win", player1, "Congratulation! 🥳🎉🤩")
   print("It takes", rounds, "!")
   break

  elif p2score == 3:
   print("Win", player2, "Congratulation! 🥳🎉🤩")
   print("It takes", rounds, "!")
   break
  


  
    
 


  

  


  

  
  

  

  
  
    


  
