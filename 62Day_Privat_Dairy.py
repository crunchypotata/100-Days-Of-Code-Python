import os, time, datetime
from replit import db

def add():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Private Dairy{timestamp}")
  print()
  text = input("Write sth: ").strip().capitalize()
  db[timestamp] = text
  
def view():
  time.sleep(1)
  os.system("clear")
  keys = db.keys()
  for key in keys:
    print(f"""{key}{db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0]=="e"):
      break
  
login = input("Enter Your Password: ").strip()
if login != "pewpew":
  print("Incorrect")
  exit()
  
while True:
  os.system("clear")
  menu = input("1.Add\n2.View\n")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  else:
    break
