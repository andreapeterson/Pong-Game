import turtle as t
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from playsound import playsound


# Screen set-up
screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Creating two paddles on opposite sides of the screen from the same class.
X_CORS = [350, -350]
COLORS = ((250, 70, 22), (0, 33, 165))
t.colormode(255)
paddles = []
for x in range(0, 2):
    paddle = Paddle()
    paddle.goto(x=X_CORS[x], y=0)
    paddle.color(COLORS[x])
    paddles.append(paddle)

# Programming the right paddle to move to up and down keys and the left paddle to move with the "w" and "s" keys.
screen.listen()
screen.onkeypress(key="Up", fun=paddles[0].up)
screen.onkeypress(key="Down", fun=paddles[0].down)
screen.onkeypress(key="w", fun=paddles[1].up)
screen.onkeypress(key="s", fun=paddles[1].down)


score = Scoreboard()
ball = Ball()
playsound('gamemusic.mp3', block=False)
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.bounce()
    if (ball.distance(paddles[0]) < 50 and 320 < ball.xcor() < 350) or (
            ball.distance(paddles[1]) < 50 and -320 > ball.xcor() > -350):
        ball.bounce_paddle()
    elif ball.xcor() > 380:
        score.l_point()
        ball.reset_position()
    elif ball.xcor() < -380:
        score.r_point()
        ball.reset_position()
