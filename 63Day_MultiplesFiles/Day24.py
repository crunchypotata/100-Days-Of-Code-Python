import random
print("Dice game")

number = int(input("How many sides?"))
attempt = "yes"

def roll_dice(number):
  print("Your rolled", random.randint(1, number))
  
while attempt == "yes":
  roll_dice(number)
  attempt = input("Roll again?")

print("Chao")
        

