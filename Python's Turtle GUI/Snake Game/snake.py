from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        '''
            Initializes a snake object with 3 segments
        '''
        for pos in STARTING_POS:
            self.add_segment(pos)
    
    def add_segment(self, pos):
        '''
            Create another segment for the snake body
        '''
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(pos)
        self.segments.append(snake)

    def increase_size(self):
       '''
            Calls add_segment to add length to the snake's 
            current body
       '''
       self.add_segment(self.segments[-1].position())

    def move(self):
        '''
            Move the body of the snake within the 
            Turtle Coordinate system 
        '''
        for segment in range(len(self.segments)-1,0,-1):
            next_x = self.segments[segment-1].xcor()
            next_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(next_x,next_y)
        
        self.head.forward(MOVE)

    def move_up(self):
        '''
            Move the snake forward by 10 spaces
        '''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def move_down(self):
        '''
            Move the snake backward by 10 spaces
        '''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def move_left(self):
        '''
            Orient the snake to the left and
            move forward by 10 spaces
        '''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  
    
    def move_right(self):
        '''
            Orient the snake to the right and
            move forward by 10 spaces
        '''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def reset_snake(self):
        '''
            Remove the current snake and reset 
            the game to the original snake length
        '''
        for snake in self.segments:
            snake.goto(1000,1000)
            
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    