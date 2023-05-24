from turtle import Turtle

TEXT_ALIGN = 'center'
FONT = 'Arial'
FONTSIZE = 24

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Python's Turtle GUI/Snake Game/data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", False, align=TEXT_ALIGN, font=(FONT, FONTSIZE, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()
        
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
