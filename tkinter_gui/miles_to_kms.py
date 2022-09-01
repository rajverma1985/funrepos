# create test grid with some buttons and entry and play with their placements.
from tkinter import *

# the main window for the calculator
window = Tk()
window.title("Miles to Km convertor")
window.minsize(width=300, height=150)
window.config(padx=40, pady=40)

# Entry for taking input
take_input = Entry(bd=2, width=10)
take_input.grid(column=1, row=0)

# Miles label
new_label = Label(font=("Arial", 18, "bold"), text="Miles")
new_label.grid(column=2, row=0)
window.config(padx=20, pady=20)

# Equals label
new_label = Label(font=("Arial", 18, "bold"), text="Equals")
new_label.grid(column=0, row=1)
window.config(padx=20, pady=20)

#kms label
new_label = Label(font=("Arial", 18, "bold"), text="KM's")
new_label.grid(column=2, row=1)
window.config(padx=20, pady=20)

# creating buttons, event on button click
button = Button(text="Calculate")
button.grid(column=1, row=2)

window.mainloop()
