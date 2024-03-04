from turtle import Turtle

ALIGNMENT = "center"
FONT_NAME = "Courier"
FONT_SIZE = 24
FONT_TYPE = "normal"
PEN_COLOUR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor(PEN_COLOUR)
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_TYPE))

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_TYPE))
