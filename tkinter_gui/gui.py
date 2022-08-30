from tkinter import *

# initialize a class TK for windows and then call the mainloop at the end to open a new
window = Tk()
window.title("Quiz Game")
window.minsize(width=500, height=600)

# creating labels
new_label = Label(font=("Arial", 24, "bold"), text="Test Label")
new_label.pack(side="top")


# buttons
def click_action():
    input_text = take_input.get()
    new_label.config(text=input_text)


# creating buttons, event on button click
button = Button(text="Click Here", command=click_action)
button.pack()

# Entry for an item, basically entry field
take_input = Entry(bd=2, width=10)
take_input.pack()

# Widgets, radio buttons, spinbox, scale, text, checkbox, listbox

# Text  box basically to create a legend for the client to type or enter
# Text
text = Text(height=10, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get a current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox for scale
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# checkbox
state = IntVar()  # keep a track of state of the box checked or not


def checkbox_state():
    print(state.get())


checkbox = Checkbutton(text="is_on", variable=state, command=checkbox_state)
state.get()
checkbox.pack()


# radio buttons, they use similar Intvar to keep a track of its state.
def radio_stat():
    print(radio_state.get())


radio_state = IntVar()
radio = Radiobutton(text="200_value", value=200, variable=radio_state, command=radio_stat)
radio2 = Radiobutton(text="100_value", value=100, variable=radio_state, command=radio_stat)
radio_state.get()
radio.pack()
radio2.pack()


# listbox
def listbox_state(check):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=5)
dbs = ['postgres', 'mongo', 'cassandra', 'oracle', 'sql server']
for db in dbs:
    listbox.insert(dbs.index(db), db)

listbox.bind("<<ListboxSelect>>", listbox_state)
listbox.pack()

# main look to keep the window open and running
window.mainloop()
