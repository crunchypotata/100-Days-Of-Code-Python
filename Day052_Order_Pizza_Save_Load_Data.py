import time, os

print("🌟Kebab pizza🌟")
print()

myOrder = []

try:
  f = open("myOrder.txt","r")
  myOrder = eval(f.read())
  f.close()
except:
  print("ERROR: there isn't pizza list, using a blank list  ")
  

def addOrder():
  name = input("Your name? ").strip().capitalize()
  amount = int(input("How many pizzas? "))
  size = (input("Which size: s/m/l? ")).strip().capitalize()
          
  cost = 0
  if size == "s":
    cost = 5.99
  elif size == "m":
    cost = 8.99
  else:
    cost = 14.99

  price = amount*cost
  price = round(price, 2)
  
  row = [name, amount, size, price]
  myOrder.append(row)

  print()
  print("Great, you pizza will be cost", price)

  time.sleep(3)
  os.system("clear")
  
def viewOrder():
  
  time.sleep(1)
  os.system("clear")
  
  h1 = "Name"
  h2 = "Amount"
  h3 = "Size"
  h4 = "Price"
  print(f"{h1:<7}{h2:^7}{h3:^7}{h4:>7}")
  print()
  for row in myOrder:
    print(f"{row[0]:<7}{row[1]:^7}{row[2]:^7}{row[3]:>7}")
  
  time.sleep(5)
  os.system("clear")


while True:
  
  menu = int(input("1.Add\n2.View\n3.Leave\n"))
  if menu == 1:
    addOrder()
  elif menu == 2:
    viewOrder()
  elif menu == 3:
    break
  else:
    print("ERROR. Please select 1, 2, or 3")
    time.sleep(1)
    os.system("clear")
  
  f = open("myOrder.txt", "w")
  f.write(str(myOrder))
  f.close()
    