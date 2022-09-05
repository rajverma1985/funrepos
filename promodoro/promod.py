import time
from tkinter import *

# TODO:
#  1. add timer HEADING on top of tomato
#  2. add reset and start labels
#  3. add clock in the tomato for changes in time
#  4.  add checkmark for cycles of work and break done
#  5. use grid instead of pack for canvas.

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

def countdown():
    window.....
def start_timer(var):
    canvas.itemconfig(timer, text=var)


# create base window for the app
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)
canvas = Canvas(width=200, height=300, bg=YELLOW, highlightthickness=0)
t_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=t_image)
timer = canvas.create_text(100, 110, text="00:00", font=("Arial", 20, "bold"))
canvas.grid(column=1, row=1)

# Timer, clock and  labels
timer_label = Label(font=("Arial", 20, "bold"), text="TIMER", bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)
tick_label = Label(font=("Arial", 20, "bold"), text="✓", bg=YELLOW, fg=GREEN)
tick_label.grid(column=1, row=3)


# Start and reset buttons
def reset_timer():
    pass


# creating buttons, event on button click
start_button = Button(height=2, width=4, text="Start", bd=0, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(height=2, width=4, text="Reset", bd=0, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Just in case Entry

window.mainloop()
