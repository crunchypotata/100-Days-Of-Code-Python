import random, time, os 

bingoNum = []  

def ran():
  number = random.randint(0,90)
  return number

def prettyPrint():
  for row in bingoNum:
    for item in row:
      print(f"{item:^5}", end=" | ")
    print()
  print()

def createCard():
  global bingoNum
  numbers = []
  for i in range(8):
    num = ran()
    while num in numbers:
      num = ran()
    numbers.append(ran())

  numbers.sort()
  
  bingoNum = [ [numbers[0], numbers[1], numbers[2]],
               [numbers[3], "BINGO", numbers[4]],
               [numbers[5], numbers[6], numbers[7]] ]

print("BINGO GENERATOR")

createCard()

while True:
  prettyPrint()
  num = int(input("Your number: ").strip())
  for row in range(3):
    for item in range(3):
      if bingoNum [row][item] == num:
        bingoNum [row][item] = "X"

  round = 0
  for row in bingoNum:
    for item in row:
      if item == "X":
        round+=1

  if round == 8:
    print("You Won!")
    break

  time.sleep(1)
  os.system("clear")
   
    

