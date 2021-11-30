from turtle import Turtle
CENTER_ALIGN = "center"
FONT_STYLE = ("courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score} ", align=CENTER_ALIGN, font=FONT_STYLE)

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over ", align=CENTER_ALIGN, font=FONT_STYLE)

