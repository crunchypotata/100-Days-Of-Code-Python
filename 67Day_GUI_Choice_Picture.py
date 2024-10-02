import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Guess Who") 
window.geometry("300x200") 

label = "Guess Who?"

def showImage():
  person = text.get("1.0", "end")
  if person.lower().strip() == "mo":
    canvas.itemconfig(container, image=mo)
  elif person.lower().strip() == "charlotte":
    canvas.itemconfig(container, image=charlotte)
  elif person.lower().strip() == "gerald":
    canvas.itemconfig(container, image=gerald)
  elif person.lower().strip() == "katie":
    canvas.itemconfig(container, image=katie)
  else:
    hello["text"] = "Unable to find this user"


hello = tk.Label(text = label) 
hello.pack() 

text = tk.Text(window, height=1, width=30)
text.pack()

button = tk.Button(text = "Find", command=showImage)
button.pack()

canvas = tk.Canvas(window, width = 400, height=350) 
canvas.pack()  

charlotte = ImageTk.PhotoImage(Image.open("Guess Who/charlotte.jpg"))
gerald = ImageTk.PhotoImage(Image.open("Guess Who/gerald.jpg"))
katie = ImageTk.PhotoImage(Image.open("Guess Who/katie.jpg"))
mo = ImageTk.PhotoImage(Image.open("Guess Who/mo.jpg"))
                        
container = canvas.create_image(150,1,image= None)


tk.mainloop()
