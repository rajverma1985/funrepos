import turtle
from turtle import Screen, Turtle
from data import df

path = './blank_states_img.gif'
screen = Screen()
screen.title("USA image game")
screen.addshape(path)
turtle.shape(path)
states = df.state.to_list()

guess = []
while len(guess) < 50:
    user_input = screen.textinput(title='Guess the states', prompt='Write the name of a state:').capitalize()
    if user_input == 'Exit':
        break
    if user_input in states:
        guess.append(user_input)
        name = Turtle()
        name.penup()
        name.hideturtle()
        co_ord = df[df.state == user_input]
        name.goto(int(co_ord.x), int(co_ord.y))
        name.write(co_ord.state.item())

