maneText = input("Write something: ")

def text(color):
  if color=="g":
    print("\033[32m", sep="", end="")
  elif color == "y":
    print("\033[1;33m", sep="", end="")
  elif color == "p":
    print("\033[1;35m", sep="", end="")
  elif color == "b":
    print("\033[0;34m", sep="", end="")
  elif color==" ":
    print("\033[0m", end="")
  elif color=="r":
    print("\033[31m", end="")
    

for letter in maneText:
  text(letter.lower())
  print(letter, end="")
