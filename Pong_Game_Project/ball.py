from turtle import Turtle
import random

SHAPE = "circle"
COLOR = "white"

#Used for changing the direction of the ball after a player scores 
delta_x_range = [-5,5]
delta_y_range = [-5,5]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.dx = random.choice(delta_x_range)
        self.dy = random.choice(delta_y_range)
        self.ball_speed = 0.05 
        self.create_ball()
   
    
    def create_ball(self):
        """Setting the properties of the self"""
        self.shape(SHAPE)
        self.color(COLOR)
    
    def move_ball(self):
        """Function for movement of the self"""
        new_x_pos = self.xcor() + self.dx
        new_y_pos = self.ycor() + self.dy
        self.goto(new_x_pos,new_y_pos)

    def wall_bounce(self):
        """Function to change the direction of the ball if it hits the wall"""
        self.dy *= -1    

    def paddle1_bounce(self, paddle):
        #This function detect if the ball collides with paddle1
        if self.xcor() <= -330 and self.xcor() > -340:
            if ((paddle.ycor() + 50) > (self.ycor())) and ((paddle.ycor() - 50) < (self.ycor())): 
                self.setx(-330)
                self.dx *= -1
                self.adjust_speed()
        elif self.xcor() < -340 and self.xcor() >= -360:
            if abs((paddle.ycor() + 50) - self.ycor()) <= 10:
                self.sety(paddle.ycor() + 60)
                self.dy *= -1
            elif abs((paddle.ycor() - 50) - self.ycor()) <= 10:
                self.sety(paddle.ycor() - 60)
                self.dy *= -1
        

    def paddle2_bounce(self, paddle):
        #This function detect if the ball collides with paddle2
        if self.xcor() >= 330 and self.xcor() < 340:
            print("x_collided")
            if ((paddle.ycor() + 50) > (self.ycor())) and ((paddle.ycor() - 50) < (self.ycor())):
                print("y_collided") 
                self.setx(330)
                self.dx *= -1
                self.adjust_speed()
        elif self.xcor() > 340 and self.xcor() <= 360:
            if abs((paddle.ycor() + 50) - self.ycor()) <= 10:
                self.sety(paddle.ycor() + 60)
                self.dy *= -1
            elif abs((paddle.ycor() - 50) - self.ycor()) <= 10:
                self.sety(paddle.ycor() - 60)
                self.dy *= -1
        
    def adjust_speed(self):
        """Function to change time.sleep function to increase the ball speed"""
        if self.ball_speed > 0.02:
            self.ball_speed -= 0.01
            return self.ball_speed

    def reset_position(self):
        """Function to determing the direction of the ball when starting the game"""
        self.dx = random.choice(delta_x_range)
        self.dy = random.choice(delta_y_range)
        self.goto(0,0)
