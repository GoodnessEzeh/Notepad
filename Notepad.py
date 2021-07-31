from tkinter import filedialog
from tkinter.constants import BOTH, END, INSERT, LEFT, TRUE, WORD
from tkinter.filedialog import *
import tkinter as tk
from typing import Text

def saveFile():
    new_file = asksaveasfile(mode='w', defaultextension=".txt")
    if new_file is None:
        return
    text = str(tk.Entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = filedialog.askopenfile(mode='r', filetype = [('text files', '.text')])
    if file is None:
        content = file.read()
    entry.insert(INSERT, content)    

def clearFile():
    entry.delete(1.0, END)   

canvas =tk.Tk()
canvas.geometry("400x600")
canvas.title("Goodness Ezeh's Notepad")
canvas.config(bg="white")
top = tk.Frame(canvas)
top.pack(padx = 10, pady=5, anchor= 'nw')

b1 = tk.Button(canvas, text="Open", bg="#ffffff", command= openFile)
b1.pack(in_ = top, side=LEFT)

b2 = tk.Button(canvas, text="Save", bg="#ff3333", command= saveFile)
b2.pack(in_ = top, side=LEFT)

b3 = tk.Button(canvas, text="Clear", bg="#00ff00", command= clearFile)
b3.pack(in_ = top, side=LEFT)

b4 = tk.Button(canvas, text="Exit", bg="#0000ff", command= exit)
b4.pack(in_ = top, side=LEFT)

entry = tk.Text(canvas, wrap= WORD, bg= "#ff4d4d", font = ("poppins", 15))
entry.pack(padx = 10, pady = 5, expand= TRUE, fill = BOTH)

canvas.mainloop()