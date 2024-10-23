import requests, json, os, time
from replit import db

while(True):
  time.sleep(1)
  os.system("clear")
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 
  
  joke = result.json()
  jk = joke["joke"]
  id = joke["id"]
  print(jk)
  print()
  
  menu = input("(s)ave joke\n(l)oad old jokes\n(n)ew joke ").lower()
  if menu == "n":
    continue
  elif menu == "s":
    db[id] = jk
    print("\nSAVED\n")
    continue  
  else:
    keys = db.keys()
    for key in keys:
      result = requests.get(f"https://icanhazdadjoke.com/j/{key}", headers={"Accept":"application/json"})
      joke = result.json()
      print(joke["joke"])
      print("\n")
      time.sleep(1)
