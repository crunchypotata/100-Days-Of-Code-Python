def text(color, word):
  if color=="green":
    print("\033[32m", word, sep="", end="")
  elif color == "yellow":
    print("\033[1;33m", word, sep="", end="")
  elif color == "purple":
    print("\033[1;35m", word, sep="", end="")
  elif color == "blue":
    print("\033[0;34m", word, sep="", end="")
  elif color == "underline":
    print("\033[4m", word, sep="", end="")
  elif color == "bold":
    print("\033[1m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")
    
    
print("Super Subroutine")
print()
print("With my ", end="")
text("yellow", "new program")
text("reset", " I can just call yellow('and') ")
text("red", "it will print in yellow ")
text("blue", "or even blue! ")
text("reset", "Nice and ")
text("underline", "Epic!")
