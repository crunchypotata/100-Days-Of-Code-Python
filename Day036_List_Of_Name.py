nameList = []

def nameOfPeople():
  print()
  for sheet in nameList:
    print(sheet)
  print()
  
while True:
  name = input("First name > ").strip().capitalize()
  surname = input("Surname > ").strip().capitalize()
  fullname = f"{name} {surname}"
  if fullname not in nameList:
    nameList.append(fullname)
  else:
    print("Ooops, dublicate name")
  nameOfPeople()

