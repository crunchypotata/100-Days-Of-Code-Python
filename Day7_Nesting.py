print("Fan question Generator")
print()
tvshow = input("What is your favorite tv show? ")
if tvshow == "Walking Dead":
  print("Oh, now! Why not Last of Us? ")
  faveCharacter = input("Who is your favorite character?: ")
  if faveCharacter == "Rick":
    print("Hmm, maybe something more interesting?")
  if faveCharacter == "Negan":
    print("Great answer!")
  else:
   print("No, the best character is Negan!" )
elif tvshow == "Last of Us":
  print("Wow, sounds great!")
  faveCharacter = input("Who is your favorite character?: ")
  if faveCharacter == "Joel":
    print("How predictable!")
  if faveCharacter == "Elly": 
    print("Not bad!")
  else:
    print("No, the best character is Joel!" )
else:
  print("Noo, Walking dead is better! ")
