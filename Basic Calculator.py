import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

# Create the main window
win = tk.Tk()
win.title('Calculator')

# Create a frame for the calculator
frame = tk.Frame(win, bg="skyblue", padx=10)
frame.pack()

# Entry widget for displaying calculations
entry = tk.Entry(frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

# Function to handle button clicks
def click(num):
    entry.insert(tk.END, num)

# Function to evaluate the expression
def equal():
    try:
        res = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, res)
    except Exception as e:
        tk.messagebox.showinfo("Error", "Syntax Error")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# List of buttons to create
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1), ('+', 5, 0), ('-', 5, 1),
    ('*', 5, 2), ('/', 6, 0)
]

# Create buttons and add them to the grid
for txt, r, c in buttons:
    tk.Button(frame, text=txt, padx=15, pady=5, width=3, command=lambda t=txt: click(t)).grid(row=r, column=c, pady=2)

# Create the Clear and Equal buttons
tk.Button(frame, text="Clear", padx=15, pady=5, width=12, command=clear).grid(row=6, column=1, columnspan=2, pady=2)
tk.Button(frame, text="=", padx=15, pady=5, width=9, command=equal).grid(row=7, column=0, columnspan=3, pady=2)

# Start the Tkinter event loop
win.mainloop()
