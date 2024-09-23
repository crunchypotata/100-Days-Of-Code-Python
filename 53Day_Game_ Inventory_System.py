import time, os
inventory = []

try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
  pass

def addInt():
  item = input("The Item to add:> ").capitalize()
  inventory.append(item)
  print(f"The {item} has been added")
  time.sleep(2)
  os.system("clear")
  
     
def viewInt():
  seen = []
  seen = set(inventory)
  for item in seen:
    print(f"{item} {inventory.count(item)}")
  time.sleep(2)
  os.system("clear")
  
  
def removeInt():
  item = input("The Item to remove:> ").capitalize()
  if item in inventory:
    inventory.remove(item)
    print(f"The {item} has been removed")
  else:
    print("You don't have that item")
  time.sleep(2)
  os.system("clear")


while True:
  print("🌟RPG Inventory🌟")
  print()
  menu = int(input("1.Add\n2.View\n3.Remove\n4.Leave\n\n> "))
  
  if menu == 1:
    addInt()
  elif menu == 2:
    viewInt()
  elif menu == 3:
    removeInt()
  elif menu == 4:
    break
  else:
    print("Choose correct number")


f = open("inventory.txt", "w")
f.write(str(inventory))
f.close()