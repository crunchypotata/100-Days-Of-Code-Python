import random

def roll_dice(sides):
  result = random.randint(1, sides)
  return result

def roll_6_and_8():
  roll_6 = roll_dice(6)
  roll_8 = roll_dice(8)
  health = roll_6 * roll_8
  return health
  
print("Character Stats Generator")
print()

attempt = "yes"

while attempt == "yes":
  name_char = input("What's name of your char? ")
  health = roll_6_and_8()
  print(name_char, "has", health, "hp")
  attempt = input("Create one more characters? ")
