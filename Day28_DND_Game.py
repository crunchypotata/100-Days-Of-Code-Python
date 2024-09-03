import os, time, random


def roll_dice(sides):
  result = random.randint(1, sides)
  return result

def health():
  health_stat = (roll_dice(6) * roll_dice(12)) / 2 + 10
  return health_stat

def strenght():
  strenght_stat = (roll_dice(6) * roll_dice(12)) / 2 + 12
  return strenght_stat


 
print("🔮😱 EPIC BATTLE 😱🔮")
print()


while True:

  char_name1 = input("Chose name for you character: ")
  char_type1 = input("Chose class of your characters: human, elf, wizard, orc: ")
  if char_type1 == "human" or char_type1 == "elf" or char_type1 == "wizard" or char_type1 == "orc":
    
    print()
    print(char_name1, ". Your class is", char_type1)
    break

  else:
    print("You have only 4 options: human, elf, wiard, orc.")
    continue

char1health = health()
char1strenght = strenght()
print("Health:", char1health)
print("Strenght:", char1strenght)
print()
print("Who are they battling?")
print()

while True:
  
  char_name2 = input("Chose name for you character: ")
  char_type2 = input("Chose class of your characters: human, elf, wizard, orc: ")
  if char_type2 == "human" or char_type2 == "elf" or char_type2 == "wizard" or char_type2 == "orc":
    
    print()
    print(char_name2, ". Your class is", char_type2)
    break

  else:
    print("You have only 4 options: human, elf, wiard, orc.")
    continue

char2health = health()
char2strenght = strenght()
print("Health:", char2health)
print("Strenght:", char2strenght)
print()

print("BATTLE TIME!")
print()

round = 1
winner = None 

while True :
  time.sleep(3)
  os.system("clear")
  
  char1_res = roll_dice(6)
  char2_res = roll_dice(6)

  difference = abs(char1strenght - char2strenght) + 1
  
  if char1_res > char2_res :
    char2health -= difference
    if round == 1:
      print("Win", char_name1)
    else:
      print(char_name1, "Wins round", round) 
  elif char2_res > char1_res :
    char1health -= difference
    if round == 1:
      print("Win", char_name2)
    else:
      print(char_name2, "Wins round", round) 
  else:
    print("Draw round")

  print()
  print(char_name1)
  print("HEALTH", char1health)
  print()
  print(char_name2)
  print("HEALTH", char2health)

  if char1health <= 0:
    print(char_name1, "has died!")
    winner = char_name2
    break
  elif char2health <= 0:
    print(char_name2, "has died!")
    winner = char_name1
    break
  else:
    print("Draw round")
    round += 1
  
time.sleep(3)
os.system("clear")

print(winner, "has won in", round, "rounds")

    
    