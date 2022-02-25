import random
from turtle import Turtle

COLORS = ['red', 'green', 'yellow', 'blue', 'purple', 'brown', 'orange']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class Cars:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.moving_speed = STARTING_MOVE_DISTANCE

    def create_new_car(self):
        rand_number = random.randint(1, 8)
        if rand_number == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=0.6, stretch_len=1.7)
            new_car.color(random.choice(COLORS))
            y_position = random.randint(-230, 230)
            new_car.goto(300, y_position)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.moving_speed)

    def speed_up(self):
        self.moving_speed += MOVE_INCREMENT



