from turtle import Turtle
import time
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.over = False
        self.pencolor("white")
        self.penup()
        self.hideturtle()

    def set_scoreboard(self):
        """Setting the scoreboard"""
        self.setposition(0,270)
        score_tracker = f"Score: {self.score}"
        self.write(score_tracker, align="center", font=("Courier", 16, "normal"))

    def update_score(self):
        """Updating the score"""
        self.score += 1
        self.clear()
        self.set_scoreboard()

    def game_over(self):
        """Displaying Game Over message"""
        self.home()
        self.write("Game Over.", align="center", font=("Courier", 16, "normal"))
        self.over = False

    def whats_next(self):
        """Displaying the instructions"""
        self.setposition(0,-40)
        self.write("Press'Y' to play", align="center", font=("Courier", 16, "normal"))
        self.setposition(-1,-60)
        self.write("Press'N' to exit", align="center", font=("Courier", 16, "normal"))
        self.score = 0

    
