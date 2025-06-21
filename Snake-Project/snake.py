from turtle import Turtle
import time

MOVE_FORWARD = 20

class Snake:

    def __init__(self):
        self.length = 3
        self.xcorr = 0
        self.snake_parts = []
        self.create_body()
        self.head = self.snake_parts[0]

    def create_body(self):
        """Create initial body of snake"""
        for part in range(self.length):
            body_part = self.new_part()
            part_corr = (self.xcorr, 0)
            body_part.goto(part_corr)
            self.snake_parts.append(body_part)
            self.xcorr -= 20

    def new_part(self):
        """Properties of new part"""
        part = Turtle(shape="square")
        part.color("white")
        part.penup()
        return part
        
    def extend_body(self):
        """add new part"""
        new_part = self.new_part() 
        new_xcorr = self.snake_parts[-1].xcor()
        new_ycorr = self.snake_parts[-1].ycor()
        new_part.goto(new_xcorr, new_ycorr)
        self.length += 1
        self.snake_parts.append(new_part)

    def move(self):
        """Function to move snake"""
        for part in reversed(self.snake_parts):
            current_index = self.snake_parts.index(part)
            if current_index > 0:
                new_coor = self.snake_parts[current_index - 1].position()
                part.goto(new_coor)
        self.head.forward(MOVE_FORWARD)

    def up(self):
        """Function to move the snake up"""
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        """Function to move the snake down"""
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        """Function to move the snake left"""
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        """Function to move the snake right"""
        if self.head.heading() != 180:
            self.head.setheading(0)
        
    def reset(self):
        """Function to reset the snake"""
        for part in self.snake_parts:
            part.reset()
        #self.snake_parts.clear()
        self.__init__()
        