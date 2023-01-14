import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_x()
    scoreboard.refresh()
    if player.ycor() == 280:
        player.start_again()
        car_manager.increase_speed()
        scoreboard.up_level()
    for car in car_manager.cars:
        # print(car.shapesize())
        y, x, z = car.shapesize()
        # print(f"y={y}, x={x}, z={z}")
        # print(f"car y = {car.ycor()}. player y = {player.ycor()}")
        if player.ycor() - 20 <= car.ycor() <= player.ycor() + 20 and car.distance(player) < ((x / 2) * 20):
            game_is_on = False

scoreboard.game_over()

screen.exitonclick()


