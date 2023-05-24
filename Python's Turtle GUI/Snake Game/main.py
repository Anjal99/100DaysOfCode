import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

# Setup the game environment
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Adding key stroke functionality
screen.listen()
screen.onkey(snake.move_up,'Up')
screen.onkey(snake.move_down,'Down')
screen.onkey(snake.move_left,'Left')
screen.onkey(snake.move_right,'Right')


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase_size()
        scoreboard.point()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset_snake()

    # Detect collision with snake itself
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()