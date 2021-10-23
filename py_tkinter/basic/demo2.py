import tkinter as tk

items = [
  "aaaa", 
  "bbbb"
]
childItems = [
  "aa1", 
  "aa2"
]

def itemClick(event, arg ):  
  print(arg)   

def newItemClick(event) : 
  print(newTaskInput.get())
  items.append(newTaskInput.get())
  print(items)
  getList()
  



root = tk.Tk()
root.title("Hello World")
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=2, column=2)



newTaskInput = tk.Entry()
newTaskInput.grid(row = 0, column = 0)
newTaskButton = tk.Button(text="ADD")
newTaskButton.grid(row = 0 , column = 1)
newTaskButton.bind("<Button>", newItemClick)



checkStartRow = 2
currentRow = checkStartRow


def getList() :
  currentRow = checkStartRow
  for idx, x in enumerate(items):
    e = tk.Checkbutton(root, text = x)
    eAdd = tk.Button(text= "ADD")
    e.grid(row = currentRow, column = 0, sticky="W")
    eAdd.grid(row = currentRow, column = 1, sticky="W")

    eAdd.bind("<Button>", lambda event, arg = x : itemClick(event, arg))  
    # eAdd.bind( "<Button>", mouseClick, x )  
    currentRow = currentRow + 1
    if x == "aaaa" :
      for cidx, cx in enumerate(childItems) : 
        ce = tk.Checkbutton(text = "  " + cx)
        ce.grid(row = currentRow, column = 0, sticky="W", padx=15)
        currentRow = currentRow + 1


getList()


root.mainloop()