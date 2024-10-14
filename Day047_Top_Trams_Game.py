import os, time, random

print("🌟Top Trumps🌟")
print()
print("Items")
print()


items = {}
items["Broccoly"] = {"Usability": 15 , "Price": 75 , "Taste": 1 , "Fancyness": 76}
items["Carrot"] = {"Usability": 90, "Price": 45 , "Taste": 45 , "Fancyness": 3}
items["Сelery"] = {"Usability": 65, "Price": 89 , "Taste": 24 , "Fancyness": 102}
items["Potato"] = {"Usability": 99, "Price": 20 , "Taste": 56 , "Fancyness": 2}

while True:
    
  user = input("Chose you card:\n\nBroccoly\nCarrot\nCelery\nPotato\n").strip().title()
  comp = random.choice(list(items.keys()))
  print()
  print("Computer has picked", comp)
  print()
  stats = input("Chose you stat:\n\nUsability\nPrice\nTaste\nFancyness\n").strip().title()
  print()
  print(f"{user}:{items[user][stats]}")
  print(f"{comp}:{items[comp][stats]}")
  print()
  
  if items[user][stats] > items[comp][stats]:
    print("Win", user)

  elif items[user][stats] < items[comp][stats]:
    print("Win", comp)
  else:
    print("Draw")
  print()
  round = input("Again?  ")
  
  if round == "y":
    time.sleep(2)
    os.system("clear")
    continue
  else:
    break

