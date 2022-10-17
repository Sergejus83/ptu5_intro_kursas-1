from tkinter import ttk
import tkinter as tk
from darbotuoju_valdimas import*

win=tk.Tk()
print_employee()

win.geometry("400x300")
win.title("Darbuotojai")
employee = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
combo = ttk.Combobox(win, values=employee)
combo.pack()
win.mainloop()