import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')

player = Player()
cars = Cars()

score = ScoreBoard()
screen.listen()
screen.onkey(player.move_left, 'a')
screen.onkey(player.move_right, 'd')
screen.onkey(player.move_up, 'w')
screen.onkey(player.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_new_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish_line():
        player.start_at_beginning()
        cars.speed_up()
        score.add_score()

screen.exitonclick()
