import os, time 
listManager = []


def list_manager():
  print() 
  for item in listManager:
    print(item)
  print() 

while True:
  print("To Do List Manager")
  print()
  menu = input("Do you want to view, add, edit, remove or delete an item from the to do list?: ")
  
  if menu == "view":
    list_manager()
  elif menu == "add":
    item = input("What would you like to add in To Do list?: ")
    listManager.append(item)
  elif menu == "edit":
    item = input("What do you want to edit?: ")
    new = input("What do you want to change it to? ")
    for i in range(0,len(listManager)):
      if listManager[i]==item:
        listManager[i]=new
  elif menu == "remove":
    item = input("What would you like to remove in To Do list: ")
    if item in listManager:
      chose = input("Are you sure you want to remove this?")
      if chose == "yes":
        listManager.remove(item)
      else:
        continue
  elif menu=="delete":
    listManager = []
  else:
      print(f"{item} was not in the list")

  time.sleep(1)
  os.system("clear")

