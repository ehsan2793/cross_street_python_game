import time
from turtle import Screen
from player import Player
from cars import Cars
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')

player = Player()
cars = Cars()


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
    # player.move_up()
    # player.move_left()

screen.exitonclick()
