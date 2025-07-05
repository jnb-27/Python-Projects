from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.CenterLine()
        self.ScoreTracker()
        

    def ScoreTracker(self):
        """Function to create te actual scoreboard"""
        self.goto(-100,230)
        self.write(self.p1_score, align="center", font=("Arial", 50, "normal"))
        self.goto(100,230)
        self.write(self.p2_score, align="center", font=("Arial", 50, "normal"))
    
    def CenterLine(self):
        """Function to create the centerline"""
        self.setheading(270)
        self.pensize(5)
        for y_value in range(300,-300, -20):
            self.goto(0, y_value)
            self.pendown()
            self.forward(10)
            self.penup()
        
            
    def UpdateScores(self, player1_score, player2_score):
        """Function to update the scores"""
        self.clear()
        self.CenterLine()
        self.p1_score = player1_score
        self.p2_score = player2_score
        self.ScoreTracker()

        if self.p1_score == 11:
            self.goto(0,0)
            self.write("Player 1 wins", align="center", font=("Arial", 50, "normal"))
            return True
        elif self.p2_score == 11:
            self.goto(0,0)
            self.write("Player 2 wins", align="center", font=("Arial", 50, "normal"))
            return True
        
            