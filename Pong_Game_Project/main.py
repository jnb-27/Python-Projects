from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

#Iniital Coordinates of two paddles
P1_INITIAL_COORDINATES = (-350,0)
P2_INITIAL_COORDINATES = (350,0)

ball_speed = 0.05

game_screen = Screen() # Creates screen object
game_screen.bgcolor("black") #Setting the background to black
game_screen.setup(width=800, height=600) #Setting the dimension of the canvass
game_screen.title("Pong Game") #Setting the title of the game on the title bar
game_screen.tracer(0) #Turns off the screen animation

scores = Scoreboard()
paddle1 = Paddle(P1_INITIAL_COORDINATES) #Creates paddle object for player 1
paddle2 = Paddle(P2_INITIAL_COORDINATES) #Creates paddle object for player 2
ball = Ball() #Creates ball object


game_screen.onkeypress(fun=paddle1.up, key="w")
game_screen.onkeypress(fun=paddle1.down, key="s")
game_screen.onkeypress(fun=paddle2.up, key="Up")
game_screen.onkeypress(fun=paddle2.down, key="Down")
game_screen.listen() #Listens for key presses

game_over = False

while not game_over:
    time.sleep(ball.ball_speed)
    game_screen.update() #Updates the sceen
    ball.move_ball() #Calling the move_ball function to move the ball

    #Detect Collision with upper wall
    if ball.ycor() > 280:
        ball.wall_bounce()
    
    #Detect Collision with lower wall
    elif ball.ycor() < -280:
        ball.wall_bounce()

    #Detects if Player1 scores
    if ball.xcor() > 380:
        scores.p1_score += 1
        #scores.p2_score = scores.p2_score
        game_over = scores.UpdateScores(scores.p1_score, scores.p2_score)
        ball.ball_speed = 0.05
        ball.reset_position()

    #Detects if Player2 scores
    elif ball.xcor() < -380:
        scores.p2_score += 1
        #scores.p1_score = scores.p1_score
        game_over = scores.UpdateScores(scores.p1_score, scores.p2_score)
        ball.ball_speed = 0.05
        ball.reset_position()
    

    if ball.xcor() > 0:
        ball.paddle2_bounce(paddle2)
    
    
    elif ball.xcor() < 0:
        ball.paddle1_bounce(paddle1)
    

game_screen.exitonclick()


