import random, os, time

print("🌟Hangman🌟")
print()

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
letterList = []
lives = 6

word = random.choice(listOfWords)

while True:
  time.sleep(2)
  os.system("clear")
  
  letter = input("Choose a letter: ").strip().lower()
  print()
  if letter in letterList:
    print("You've already pinned")
    continue
    
  letterList.append(letter)
  if letter in word:
    print("Yoy find the letter")
  else:
    print("No, it isn't there")
    lives -= 1

  allLetter = True
  for i in word:
    if i in letterList:
      print(i, end='')    
    else:
      print("_", end='')
      allLetter = False
  print()
    
    
  if allLetter:
    print(f"You win with {lives} lives!")
    break
    
  if lives<=0:
    print(f"You lost! The answer was {word}")
    break
  else:
   print()
   print(f"You have only {lives}")
  
      
    
    
