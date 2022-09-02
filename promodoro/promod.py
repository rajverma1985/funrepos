from tkinter import *
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

# create base window for the app

window = Tk()
window.title("promodoro")
window.config(padx=100, pady=100, bg="YELLOW")
canvas = Canvas(width=200, height=300, bg="YELLOW", highlightthickness=0)
t_image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 100, image=t_image)
canvas.pack()

window.mainloop()