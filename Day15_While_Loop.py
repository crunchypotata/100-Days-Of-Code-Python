print("Sound of Animal")
print()

exit = "" 
while exit != "yes":
  
  animal = input("What animal do you want to hear? ")
  print()
  
  if animal == "cow":
    print("A cow says moo")
  elif animal == "cat":
    print("A cat says meow")
  else:
    print("I don't know this animal. Try one more!")
    
  exit = input("Do you want to leave? ")
  if exit == "no":
    print("😌")
    
  # else:
  #   print("Hmm. Try one more!")
  print()

print("😤")


