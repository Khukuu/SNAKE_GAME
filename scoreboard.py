from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 19, 'bold')

class scoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.scoreDisplay()
    
        
    def scoreDisplay(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"Score: {self.score}", False, align = ALIGNMENT, font = FONT)
        
            
    def addScore(self):
        self.score += 1
        print("add one")
    
    #game over sequence
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, align = ALIGNMENT, font = FONT)