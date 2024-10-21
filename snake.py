from turtle import Turtle
STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    
    def create_snake(self):
        for pos in STARTING_POS:
            self.add(pos)
            
    def add(self, position):
        newSnake = Turtle("square")
        newSnake.penup()
        newSnake.color("white")
        newSnake.goto(position)
        self.snake.append(newSnake)
        
    #for extending the snake    
    def extend(self):
        self.add(self.snake[-1].pos())
        
    def move(self):
        for seg_num in range(len(self.snake)-1, 0, -1):
            newX = self.snake[seg_num - 1].xcor()
            newY = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)
        
        
#movement
    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)
    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)
    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    
 