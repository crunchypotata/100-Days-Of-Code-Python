import os, time, datetime
from replit import db

def add():
  tweet = input("Your genial thought: ").strip().capitalize()
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}" 
  db[key] = tweet
  time.sleep(1)
  os.system("clear")
  
def view():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.3)
    counter+=1
    if(counter%10==0):
      next = input("Next 10?: ")
      if(next.lower()=="no"):
        break
  time.sleep(1)
  os.system("clear")
  
while True:
  print("Twitter")
  print()
  menu = input("1.Add\n2.View\n")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  else:
    break
  


