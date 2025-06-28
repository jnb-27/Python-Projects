from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_border import GameBorder
import time

#This variable is used to prevent triggering the function related to keys 'Y' and 'N'
GAME_IS_ON = False 

#=================Screen Settings============================
game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("Snake Game")
game_screen.tracer(0)
#============================================================

#==============Creating objects==============================
border = GameBorder()
scoreboard = Scoreboard()
snake = Snake()
food = Food()
#============================================================

border.draw_border() #Creating borders
game_screen.update() #Updating the screeen
time.sleep(0.1) #Delay 0.1s
scoreboard.set_scoreboard() #Setting the scoreboard
scoreboard.whats_next() #Displaying instruction. 'Y' to play. 'N' to exit.

#============================================================
def y_pressed():
    """Function when letter y is pressed"""
    global GAME_IS_ON
    if GAME_IS_ON == False: 
        scoreboard.clear()
        snake.reset()
        GAME_IS_ON = True
        snake_game(True)
#============================================================

#============================================================
def n_pressed():
    """Function when letter n is pressed"""
    global GAME_IS_ON
    if GAME_IS_ON == False: 
        GAME_IS_ON = True
        game_screen.bye() #Exits the turtle screen
#============================================================
        

#======Keys to check and there correspinding functions=======
game_screen.onkey(fun=snake.up, key="Up")
game_screen.onkey(fun=snake.down, key="Down")
game_screen.onkey(fun=snake.left, key="Left")
game_screen.onkey(fun=snake.right, key="Right")
game_screen.onkey(fun=y_pressed, key='Y')
game_screen.onkey(fun=n_pressed, key='N')
game_screen.listen()
#============================================================

#============================================================
def snake_game(game_start):
    """Function of the snake game"""
    global GAME_IS_ON
    
    scoreboard.set_scoreboard()

    
    while game_start:
        game_screen.update()
        time.sleep(0.1)
        snake.move()

        #Check if food is eaten
        if snake.head.distance(food) < 15:
            scoreboard.update_score()
            food.new_food()
            snake.extend_body()

        #Check if snake bumps the wall
        if snake.head.xcor() >= 270 or snake.head.xcor() <= -270 or snake.head.ycor() >= 270 or snake.head.ycor() <= -270:
            print("Snake bump the wall. You lost!")
            scoreboard.game_over()
            game_start = False
            GAME_IS_ON = False

        
        #Check if snake bumps to itself/len(snake.snake_parts)
        for part in range(1, snake.length - 1):
            if snake.head.distance(snake.snake_parts[part]) < 15:
                scoreboard.game_over()
                game_start = False
                GAME_IS_ON = False

    scoreboard.whats_next()
  
 #============================================================                
             
game_screen.exitonclick()