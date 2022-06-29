import turtle
import pandas

screen = turtle.Screen()
screen.title("India Map")
# /Users/1954513/Desktop/#100_Days_of_Python/#25-Day/
image = 'indiamap.gif'
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv('storage.csv')

cnt = 0
while cnt < len(data.states):
    answer_state = screen.textinput(title = f'You need to guess {len(data.states)- cnt}', prompt = 'Enter your state: ')
    if answer_state in list(data.states):
        row = data[data.states == answer_state]
        cnt += 1
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        x, y = int(row.x), int(row.y)
        t.goto(x, y)
        t.pensize(2)
        t.write(answer_state)

screen.exitonclick()
