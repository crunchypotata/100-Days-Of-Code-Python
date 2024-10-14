import random, os, time

print("🌟Idea Storage🌟")
print()

def append():
  f = open("my.ideas", "a+")
  ideas = input("Input your idea >  ")
  f.write(f"{ideas}\n")
  f.close()
  time.sleep(1)
  os.system("clear")

def random_idea():
  f = open("my.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  ideas = random.choice(ideas)
  print(ideas)
  
  time.sleep(1)
  os.system("clear")
  
  
while True:

  option = input("Add an idea or see a random idea? a/r > ")

  if option == "a":
    append()
            
  elif option == "r":
    random_idea()

  exit = input("Exit? y/n ")
  if exit == "n":
    continue
  elif exit == "y":
    break
    


    
    
  
    

  
                 
