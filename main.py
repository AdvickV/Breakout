import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
from blocks import BlocksManager


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle()
ball = Ball()
blocks_manager = BlocksManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(key="Left", fun=paddle.go_left)
screen.onkeypress(key="Right", fun=paddle.go_right)

while True:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    # Detect collision with blocks
    for block in blocks_manager.YELLOW_BLOCKS:
        if ball.distance(block) <= 50:
            ball.bounce_y()
            scoreboard.score += 1
            scoreboard.write_score()
            ball.increase_speed()
            blocks_manager.remove_block(block, "YELLOW")
    for block in blocks_manager.GREEN_BLOCKS:
        if ball.distance(block) <= 50:
            ball.bounce_y()
            scoreboard.score += 3
            scoreboard.write_score()
            ball.increase_speed()
            blocks_manager.remove_block(block, "GREEN")
    for block in blocks_manager.ORANGE_BLOCKS:
        if ball.distance(block) <= 50:
            ball.bounce_y()
            scoreboard.score += 5
            scoreboard.write_score()
            ball.increase_speed()
            blocks_manager.remove_block(block, "ORANGE")
    for block in blocks_manager.RED_BLOCKS:
        if ball.distance(block) <= 50:
            ball.bounce_y()
            scoreboard.score += 7
            scoreboard.write_score()
            ball.increase_speed()
            blocks_manager.remove_block(block, "RED")

    # Detect collision with paddle
    if paddle.distance(ball) < 50 and ball.ycor() < -253:
        ball.bounce_y()

    # Detect collision with wall
    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.xcor() >= 390 or ball.xcor() <= -390:
        ball.bounce_x()

    # Detect GAME OVER
    if ball.ycor() == -300:
        scoreboard.game_over()
        break


screen.exitonclick()






