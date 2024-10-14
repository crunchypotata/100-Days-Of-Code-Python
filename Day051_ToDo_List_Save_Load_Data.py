import time, os

print("🌟Life Organizer🌟")
print()

org = []

f = open("Todo.txt", "r")
org = eval(f.read())
f.close()

def add():
  time.sleep(1) 
  os.system("clear")

  case = input("What is the task? > ").strip().capitalize()
  data = input("When is it due by? > ").strip().capitalize()
  priority = input("What is the priority? > ").strip().capitalize()
  row = [case, data, priority]
  org.append(row)
  print("Thanks, this task has been added.")

def view():
  time.sleep(1) 
  os.system("clear")
  options = input("1. By name\n2. By priority\n")
  if options =="1":
    for row in org:
      for item in row:
        print(f"{item:^5}", end=" | ")
      print()
    print()
  else:
    priority = input("What priority? ").strip().capitalize()

    for row in org:
      for priority in row:
        print(f"{priority:^5}", end=" | ")
      print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1) 
  os.system("clear")

  name = input("What is the name of the record to change?").strip().capitalize() 
  found = False
  for row in org: 
    if name in row:
      found = True

  if not found:
    print("Couldn't find that")
    return
  for row in org:
    if name in row:
      org.remove(row)
      case = input("What is the task? > ").strip().capitalize()
      data = input("When is it due by? > ").strip().capitalize()
      priority = input("What is the priority? > ").strip().capitalize()
      row = [case, data, priority]
      org.append(row)
      print("Thanks, this task has been added.")

def remove():
  time.sleep(1) 
  os.system("clear")

  name = input("What is the name of the record to delete?").strip().capitalize() 
  for row in org: 
    if name in row:
      org.remove(row)

while True:

  menu = input("1. Add\n2. View\n3. Edit\n4. Remove\n").strip().capitalize()
  if menu == "1":
    add() 
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()

  f = open("Todo.txt", "w")
  f.write(str(org))
  f.close()

  time.sleep(2) 
  os.system("clear")






