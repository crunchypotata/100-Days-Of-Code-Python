import os
import time
import random



def name_char():
  while True:
    type = input("Chose class of your characters: human, elf, wizard, orc: ")
    if type == "human" or type == "elf" or type == "wizard" or type == "orc":
      print()
      print("Name of your character:", name, ". Your class is", type, ". Welcome!")
      break

    else:
      print("You have only 4 options: human, elf, wiard, orc.")
    continue
  

def roll_dice(sides):
  result = random.randint(1, sides)
  return result

def health():
  roll_6 = roll_dice(6)
  roll_12 = roll_dice(12)
  health = (roll_6 * roll_12) / 2 + 10
  return health


def strenght():
  roll_6 = roll_dice(6)
  roll_12 = roll_dice(12)
  strenght = (roll_6 * roll_12) / 2 + 12
  return strenght


  
print("🔮 Character Builder 🔮")
print()

while True:
 name = input("Chose name for you character: ")
 print()
 name_char()
 print()
 print("You health is", health())
 print("You strenght is", strenght())
 time.sleep(5)
 os.system("clear")
 round = input("Do you want to continue? ")
 if round == "no":
   print("Bye!")
   time.sleep(2)
   os.system("clear")
   break
 
 
 
