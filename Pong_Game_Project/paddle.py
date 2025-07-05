from turtle import Turtle

SHAPE = "square"
COLOR = "white"
PADDLE_HEIGHT = 5
PADDLE_WIDTH = 1
CANVASS_HEIGHT = 600

class Paddle(Turtle):

    def __init__(self, initial_coordinates):
        super().__init__()
        self.penup()
        self.coordinates = initial_coordinates
        self.create_paddle()

    def create_paddle(self):
        """Function to create paddles"""
        self.color(COLOR)
        self.shape(SHAPE)
        self.goto(self.coordinates)
        self.shapesize(stretch_wid=PADDLE_HEIGHT, stretch_len=PADDLE_WIDTH, outline=1)

    def up(self):
        """Function to move up the paddle"""
        x_coor = self.xcor()
        distance_to_canvass = (CANVASS_HEIGHT / 2) -  (50 + self.ycor())
        if distance_to_canvass > 10:
            y_coor = self.ycor() + 20
            self.goto(x_coor,y_coor)
    
    def down(self):
        """Function to move down the paddle"""
        x_coor = self.xcor()
        distance_to_canvass = (CANVASS_HEIGHT / 2)  + (self.ycor() - 50)
        if distance_to_canvass > 10: 
            y_coor = self.ycor() - 20
            self.goto(x_coor,y_coor)