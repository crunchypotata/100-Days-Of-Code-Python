print("\033[32m == Guess the number!== \033[0m ")
print()

number = 14500
attempts = 0

while True :
  
  guess = int(input("Choose you number: "))
  attempts += 1
  
  if guess < number:
   print("Too low")
   print()
  elif guess > number:
   print("Too high")
   print()
  elif guess == number:
   print()
   print("You win! \033[32m Congratulation!\033[0m ")
   print("You guessed the number in", "\033[32m", attempts, "\033[0m attempts!")
   break
    
  else:
   print("No, it's not a number! Try one more")


  