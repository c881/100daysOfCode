from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []
        self.create_cars()

    def create_cars(self):
        for idx in range(2):
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_len=random.randint(1,4), stretch_wid=1)
            car.setheading(-180)
            car.goto(x=random.randint(300, 650), y=random.randint(-250, 250))
            self.cars.append(car)

    def move_x(self):
        for idx in range(len(self.cars)):
            self.cars[idx].forward(self.move_distance)
            if self.cars[idx].xcor() < -330:
                self.cars[idx].goto(x=320, y=random.randint(-250, 250))

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT



