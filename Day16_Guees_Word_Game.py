print("Guess the word")
attempts = 0

while True:

  attempts += 1
  word = input("Never going to ______ you up: ")
  
  if word == "give":
    break
  else:
   print("Nope, try again")
print("Well done! You guessed the word in", attempts, "attempts!")