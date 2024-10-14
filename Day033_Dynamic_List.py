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
  menu = input("view, add or edit?: ")
  if menu == "view":
    list_manager()
  elif menu == "add":
    item = input("What would you like to add in To Do list?: ")
    listManager.append(item)
  elif menu == "edit":
    item = input("What would you like to remove in To Do list: ")
    if item in listManager:
      listManager.remove(item)
    else:
      print(f"{item} was not in the list")
  
  time.sleep(1)
  os.system("clear")
