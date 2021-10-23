import tkinter as tk
root = tk.Tk()

root.title("Hello World")
root.geometry('600x400+50+50')
tk.Button(root, text="Make me a Sandwich").pack()

text_entry = tk.Text(root)
text_entry.pack()

tk.Checkbutton(root, text = 'Username').pack()


root.mainloop()