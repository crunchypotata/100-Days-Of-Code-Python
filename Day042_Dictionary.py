print("MokéBeast")
print()

character = {"Name": None, "Type": None, "Move": None, "Hp": None, "Mp": None}

for name, value in character.items():
  character[name] = input(f"{name}:\t").strip().title()

  
if character["Type"] == "Earth":
  print("\033[32m", end="")
elif character["Type"] == "Water":
  print("\033[34m", end="")
elif character["Type"] == "Air":
  print("\033[37m", end="")
elif character["Type"] == "Fire":
  print("\033[31m", end="")
else:
  print("\033[35m", end="")
    
print()
for name, value in character.items():
  print(f"{name:<15}: {value}")
