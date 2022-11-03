import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


screen.listen()
p1 = Player()
screen.onkey(p1.move, 'Up')

car_mngr = CarManager()
score = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_mngr.make_car()
    car_mngr.move()
    score.lvl()

    # detect collision with car:
    for car in car_mngr.cars:
        if p1.distance(car) <= 20:
            score.game_over()
            game_is_on = False
    
    if p1.passed():
        p1.reset()
        score.level += 1
        car_mngr.level_up()




screen.exitonclick()