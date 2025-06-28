from turtle import Turtle
import time

PATH = "C:/Users/thoro/Desktop/Lectures & Projects/PYTHON/Udemy Courses/100 Days of Python/Day24/Project_Snake_Game_V2/high_score.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        
        with open(PATH, mode="r") as file:
            self.high_score = int(file.read())
        
        self.over = False
        self.pencolor("white")
        self.penup()
        self.hideturtle()

    def set_scoreboard(self):
        """Setting the scoreboard"""
        self.setposition(-150,270)
        score_tracker = f"Score: {self.score}"
        self.write(score_tracker, align="center", font=("Courier", 16, "normal"))
        self.goto(150,270)
        self.write(f"High Score:{self.high_score}", align="center",font=("Courier", 16, "normal"))


    def update_highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(PATH, mode="w") as file:
                file.write(str(self.high_score))

    def update_score(self):
        """Updating the score"""
        self.score += 1
        self.clear()
        self.set_scoreboard()

    def game_over(self):
        """Displaying Game Over message and updating high score"""
        self.update_highscore()
        self.clear()
        self.set_scoreboard()
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

    
