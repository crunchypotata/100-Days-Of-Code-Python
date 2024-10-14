import os, time

print("MokéBeast")
print()

character = {}

def prettyPrint():
  print()
  for key, value in character.items():
    print(key, end= ": ")
    for subKey, subValue in value.items(): 
      print(subKey, ":", subValue, end=" | ")
    print()
          
while True:

  name = input("Name: ").strip().title()
  type = input("Type: ").strip().title()
  move = int(input("Move: "))
  hp = int(input("Hp: "))
  mp = int(input("Mp: "))
  
  character[name] = {"Type":type, "Move":move, "Hp":hp, "Mp":mp}
  
  prettyPrint()
  
  print()
  add = input("One more? ")
  if add == "y" :
    time.sleep(1)
    os.system("clear")
    continue  
  else:
    break
    
  
