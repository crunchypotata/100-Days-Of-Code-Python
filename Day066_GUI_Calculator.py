import tkinter as tk

window = tk.Tk()
window.title("Calculator") 
window.geometry("400x200") 

answer = 0
lastNum = 0
op = None

def buttonChoice(value):
  global answer
  answer = f"{answer}{value}"
  answer = int(answer) 
  hello["text"] = answer

def calcAns(thisOp):
  global answer, lastNum, op
  lastNum = answer
  answer = 0
  if thisOp == "+":
    op = "+"
  elif thisOp == "-":
    op = "-"
  elif thisOp == "*":
    op = "*"
  elif thisOp == "/":
    op = "/"
  hello["text"] = answer

def calc():
  global answer, lastNum, op
  print(f"{lastNum}\t{answer}\t{op}")
  answer = int(answer)
  if op == "+":
    total = lastNum + answer
  elif op == "-":
    total = lastNum - answer
  elif op == "*":
    total = lastNum * answer
  elif op == "/":
    total = lastNum / answer
  else: 
    total = "Error" 
  
  answer = total
  hello["text"] = answer

def clearAll():
  global answer, lastNum, op
  answer = 0
  lastNum = 0
  op = None
  hello["text"] = answer
    
hello = tk.Label(text = answer)
hello.grid(row=0, column=1)

one = tk.Button(text = "1", command = lambda:
buttonChoice(1))
one.grid(row=2, column=0)

two =tk.Button(text = "2", command = lambda: buttonChoice(2))
two.grid(row=2, column=1)

three = tk.Button(text = "3", command = lambda: buttonChoice(3))
three.grid(row=2, column=2)

add = tk.Button(text = "+", command = lambda: calcAns("+"))
add.grid(row=2, column=3)

minus = tk.Button(text = "-", command = lambda: calcAns("-"))
minus.grid(row=2, column=4)

four = tk.Button(text = "4", command = lambda: buttonChoice(4))
four.grid(row=3, column=0)

five = tk.Button(text = "5", command = lambda: buttonChoice(5))
five.grid(row=3, column=1)

six = tk.Button(text = "6", command = lambda: buttonChoice(6))
six.grid(row=3, column=2)

mult = tk.Button(text = "*", command = lambda: calcAns("*"))
mult.grid(row=3, column=3)

div = tk.Button(text = "/", command = lambda: calcAns("/"))
div.grid(row=3, column=4)

seven = tk.Button(text = "7", command = lambda: buttonChoice(7))
seven.grid(row=4, column=0)

eight = tk.Button(text = "8", command = lambda: buttonChoice(8))
eight.grid(row=4, column=1)

nine = tk.Button(text = "9", command = lambda: buttonChoice(9))
nine.grid(row=4, column=2)

zero = tk.Button(text = "0", command = lambda: answer)
zero.grid(row=5, column=1)

equals = tk.Button(text ="=", command = calc)
equals.grid(row=5, column=3)

clear = tk.Button(text = "c", command = clearAll)
clear.grid(row=5, column=4)

tk.mainloop()
  