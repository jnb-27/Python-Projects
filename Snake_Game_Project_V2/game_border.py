from turtle import Turtle

class GameBorder(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.goto(-270,270)

    def draw_border(self):
        """Function to create border"""
        self.pendown()
        for _ in range(4):
            self.forward(540)
            self.right(90)
