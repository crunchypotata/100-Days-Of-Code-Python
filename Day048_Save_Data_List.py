import os, time

print("HIGH SCORE BOARD")
print()

while True:
  
  score = input("Input your initials, score > ").split()
  f = open("high.score", "a+")
  f.write(f"{score}\n")
  print()
  print("Added to high score table")
  
  time.sleep(1)
  os.system("clear")

  more = input("Add another? y/n? > ")
  if more == "y":
    continue
  else:
    break
  
f.close()

