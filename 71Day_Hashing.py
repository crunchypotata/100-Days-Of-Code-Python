import random, os, time
from replit import db

print("🌟Login System🌟")
print()
    
def addUser():
  time.sleep(1)
  os.system("clear")
  userName = input("Login: ")
  password = input("Password: ")
  keys = db.keys()
  if userName in keys:
    print("ERROR: Username exists")
    return
    
  salt = random.randint(1000,9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)

  db[userName]={"password": newPassword, "salt": salt}

  print("User added")
    
def login():
  time.sleep(1)
  os.system("clear")
  userName = input("Login: ") 
  password = input("Password: ")
  keys = db.keys()
  if userName not in keys:
    print("ERROR: Username does not exists")
    return
  salt = db[userName]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword) 

  if db[userName]["password"] == newPassword:
    print("Login successful")
  else:
    print("Username or password incorrect")
  
  
  
while True:
  menu = input("1. Add\n2. Login\n")
  if menu == "1":
    addUser()
  elif menu == "2":  
    login()
  else:
    keys = db.keys()
    for key in keys:
      print(db[key])