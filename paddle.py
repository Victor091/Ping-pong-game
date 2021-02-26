from turtle import Turtle

WIDTH = 1
HEIGHT = 5
COLOR = 'white'
SPEED = 25  #Que tan rápido se mueve la barra
LIMITS = 243


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__(shape='square')
        self.turtlesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.penup()
        self.color(COLOR)
        self.goto(position)
        self.setheading(90)

    def move_up(self):
        if self.ycor() < LIMITS:
            self.forward(SPEED)

    def move_down(self):
        if self.ycor() > -LIMITS:
            self.backward(SPEED)

