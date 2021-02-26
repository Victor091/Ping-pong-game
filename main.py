from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard
from table import Table

#Constantes
WIDTH = 800
HEIGHT = 600
COLOR_BG = 'Black'
POSITION_USER1 = (-350, 0)
POSITION_USER2 = (350, 0)

#Instancias de objetos
screen = Screen()
screen.tracer(0)
paddle_user1 = Paddle(POSITION_USER1)
paddle_user2 = Paddle(POSITION_USER2)
ball = Ball()
score = Scoreboard()
table = Table()

#Escuchar los comandos del teclado
screen.listen()

#Comdando usuario 1
screen.onkeypress(key='w', fun=paddle_user1.move_up)
screen.onkeypress(key='s', fun=paddle_user1.move_down)

#Comandos usuario 2
screen.onkeypress(key='Up', fun=paddle_user2.move_up)
screen.onkeypress(key='Down', fun=paddle_user2.move_down)

#Configuración ventana
screen.setup(WIDTH, HEIGHT) #Cambia las dimensiones de la ventana
screen.bgcolor(COLOR_BG)
screen.title('Pong') #Agrega un nombre a la parte superior de la vetana

game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball(paddle_user1,paddle_user2,score)
    sleep(0.07)

    if score.score_user1 == 7 or score.score_user2 == 7:
        game_is_on = False
        ball.hideturtle()
        table.clear()
        score.game_over()

screen.exitonclick()