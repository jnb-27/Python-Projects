from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.new_food()

    def new_food(self):
        """Function for creating and placing the food"""
        self.reset()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.speed("fastest")
        x_position = random.randint(-260,260)
        y_position = random.randint(-260,260)
        food_position = (x_position,y_position)
        self.goto(food_position)
