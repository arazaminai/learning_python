from turtle import Turtle, Screen, clear, reset

tim = Turtle()
screen = Screen()

def move_front():
    tim.forward(10)

def move_back():
    tim.back(10)

def move_down():
    tim.right(10)

def move_up():
    tim.left(10)

def home():
    screen.resetscreen()
    

screen.listen()
screen.onkey(move_front, "w")
screen.onkey(move_back, "s")
screen.onkey(move_up, "a")
screen.onkey(move_down, "d")
screen.onkey(home, "c")

screen.exitonclick()
    