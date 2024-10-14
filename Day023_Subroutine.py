

def login():
  
  while True:
  
    user_name = input("What is your username? ")
    password = input("What is your password? ")
    if user_name == "Alex" and password == "Pewpew":
      print("Welcome to Replit!")
      break

    else:
      print("No, try one more time")
      continue

print("Replit Login System")
login()
