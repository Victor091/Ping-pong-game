from turtle import Turtle

COLOR = 'white'
STEPS = 20
WIDTH = 5


class Table(Turtle):

    def __init__(self):
        super().__init__(shape='square')
        self.color(COLOR)
        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.setheading(270)
        self.pen(pensize=WIDTH)

        #Este bloque sirve para hacer las franjas que dividen la cancha
        while self.ycor() > -280:
            self.forward(STEPS)
            self.penup()
            self.forward(STEPS)
            self.pendown()

        self.hideturtle()