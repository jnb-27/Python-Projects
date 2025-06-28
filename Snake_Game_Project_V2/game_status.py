from turtle import Turtle, Screen
from snake import Snake
from main import snake_game
class GameStatus:

    def __init__(self):
        self.screen = Screen()
        self.text = Turtle()
        self.proceed = False 

    def whats_next(self):
        self.text.pencolor("white")
        self.text.penup()
        self.text.hideturtle()
        self.text.setposition(0,-30)
        self.text.write("Press'Y' to play", align="center", font=("Courier", 16, "normal"))
        self.text.setposition(-1,-50)
        self.text.write("Press'N' to exit", align="center", font=("Courier", 16, "normal"))

    # def y_pressed(self):
    #     print("This is ok")
    #     snake_game(True)
            


            