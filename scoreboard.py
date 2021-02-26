from turtle import Turtle

COLOR = 'white'
POSITION = (0, 200)
ALIGN = 'center'
FONT = ('Courier', 80, 'normal')
FONT_OVER = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.score_user1 = 0
        self.score_user2 = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.goto(POSITION)
        self.write("{}  {}".format(self.score_user1, self.score_user2), align=ALIGN, font=FONT)

    def add_point(self, user):
        if user == 'user1':
            self.score_user1 += 1
        else:
            self.score_user2 += 1

        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        if self.score_user1 == 7:
            winner = 'Left user wins!'
        else:
            winner = 'Right user wins!'

        self.write(winner, align=ALIGN, font=FONT_OVER)