# create test grid with some buttons and entry and play with their placements.
from tkinter import *

window = Tk()
window.title("Quiz Game")
window.minsize(width=600, height=400)

# creating labels
new_label = Label(font=("Arial", 24, "bold"), text="Test Label")
new_label.grid(column=0, row=0)


# creating buttons, event on button click
button = Button(text="Click Here")
button.grid(column=1, row=1)

# Entry for an item, basically entry field
take_input = Entry(bd=2, width=10)
take_input.grid(column=3, row=3)

button = Button(text="New button")
button.grid(column=2, row=0)

window.mainloop()
