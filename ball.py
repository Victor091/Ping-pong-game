from turtle import Turtle
from random import randint
from scoreboard import Scoreboard

WIDTH = 1
HEIGHT = 1
INITIAL_SPEED = 10
COLOR = 'white'
LIMITS_WALL = 280


class Ball(Turtle):

    def __init__(self):
        super().__init__(shape='circle')
        self.turtlesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.user = 'user'
        self.penup()
        self.initial_push()
        self.color(COLOR)
        self.speed_ball = INITIAL_SPEED

    def move_ball(self, pad1, pad2, score: Scoreboard):

        #Detectando si salio de los limites
        if self.xcor() < -360 or self.xcor() > 360:
            self.goto(0, 0)
            score.add_point(self.user)
            self.initial_push()
        #Detectando si pego con el paddle del usuario 1
        elif self.distance(pad1) <= 50 and self.xcor() < -325:
            self.user = 'user1'
            self.collision_paddle_user1(pad1)
            self.speed_ball += 1
        # Detectando si pego con el paddle del usuario 2
        elif self.distance(pad2) <= 50 and self.xcor() > 325:
            self.user = 'user2'
            self.collision_paddle_user2(pad2)
            self.speed_ball += 1
        #Detectando colosion con la pared superior
        elif self.ycor() > LIMITS_WALL:
            self.collision_wall_up()
        #Detectando colosion con la pared inferior
        elif self.ycor() < -LIMITS_WALL:
            self.collision_wall_down()

        #Velocidad de la pelota
        self.forward(self.speed_ball)

    #Colosion con la parte de arriba, redirige la bola
    def collision_wall_up(self):
        #El angulo de giro es de 54°
        if self.user == 'user1':
            self.setheading(306) #360° - 54°
        else:
            self.setheading(234) #180° + 54

    #Colision con la parte de abajo, redirige la bola
    def collision_wall_down(self):
        #El angulo de gira es de 54°
        if self.user == 'user1':
            self.setheading(45)
        else:
            self.setheading(126) #180°-54°

    def collision_paddle_user1(self,pad1):
        posibility = randint(0, 1)
        if posibility == 0:
            self.setheading(randint(0, 54))
        else:
            self.setheading(randint(306, 360))

    def collision_paddle_user2(self,pad2):
        self.setheading(randint(126, 234))

    def initial_push(self):
        self.speed_ball = INITIAL_SPEED
        twist = randint(0, 360)
        self.setheading(twist)
        # Este bloque sirve para controlar si la pelota le dio para el campo de cierto jugador
        if 0 <= twist <= 90 or 270 <= twist <= 360:
            self.user = 'user1'
        else:
            self.user = 'user2'



