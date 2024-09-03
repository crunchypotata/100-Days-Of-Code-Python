def text(color, word):
  if color=="green":
    print("\033[32m", word, sep="", end="")
  elif color == "yellow":
    print("\033[1;33m", word, sep="", end="")
  elif color == "purple":
    print("\033[1;35m", word, sep="", end="")
  elif color == "blue":
    print("\033[0;34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")
    
text("purple","=")
text("reset","=")
text("blue","=")
text("yellow", " Music App ")
text("blue","=")
text("reset","=")
text("purple","=")
print()
print()
text("reset", "Radio GAGA\n")

title = "Queen"
title2 = "WELCOME TO"
title3 = "-- ARMBOOK --"
prev = "PREV"
next = "NEXT"
pause = "PAUSE"

text("yellow", f"{title}")
print()
print()
text("reset", f"{prev}\n") 
text("green", f"{next: ^15}\n")  
text("purple", f"{pause: ^25}\n")

print()
print()

text("reset", f"{title2: ^35}\n")
print()
text("blue", f"{title3: ^35}")

print()
print()
menu_text = "Definitely not a rip off "
text("yellow", f"{menu_text: >35}\n")
menu_text = "a certain other social "
text("yellow", f"{menu_text: >35}\n")
menu_text = "networking site"
text("yellow", f"{menu_text: >34}\n")

print()
print()

title3 = "Honest."
text("purple", f"{title3: ^35}\n")
print()
username = "Username:"
password = "Password:"
text("reset", f"{username: ^35}\n")
text("reset", f"{password: ^35}\n")
