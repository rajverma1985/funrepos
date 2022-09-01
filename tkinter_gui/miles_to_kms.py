# create test grid with some buttons and entry and play with their placements.
from tkinter import *

# the main window for the calculator
window = Tk()
window.title("Miles to Km convertor")
window.minsize(width=300, height=150)
window.config(padx=40, pady=40)


def cal_button():
    input_text = float(take_input.get())
    if type(input_text)  is float:
        kms_in_miles = "{:.2f}".format(1.6 * input_text)
        results.config(text=kms_in_miles)
    else:
        results.config(text="Please enter an integer")


# Entry for taking input
take_input = Entry(bd=2, width=5)
take_input.grid(column=1, row=0)

# Miles label
miles = Label(font=("Arial", 18), text="Miles")
miles.grid(column=2, row=0)
window.config(padx=20, pady=20)

# Equals label
equals = Label(font=("Arial", 18), text="Equals")
equals.grid(column=0, row=1)
window.config(padx=20, pady=20)

# results label
results = Label(font=("Arial", 18, "bold"), text="0")
results.grid(column=1, row=1)
window.config(padx=20, pady=20)

#kms label
kms = Label(font=("Arial", 18), text="KM's")
kms.grid(column=2, row=1)
window.config(padx=20, pady=20)

# creating buttons, event on button click
calculate = Button(text="Calculate", command=cal_button)
calculate.grid(column=1, row=2)

window.mainloop()
