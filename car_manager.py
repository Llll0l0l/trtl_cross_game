from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
        
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self):

        random_chance = random.randint(1, 6)

        if random_chance == 1:
            
            car = Turtle()
            car.penup()
            # change shape
            car.shape('square')
            # stretch the size
            car.shapesize(1, 2) 
            # change color
            rand_color = random.choice(COLORS)
            car.color(rand_color)
            # add to the list
            self.cars.append(car)

            # random y position
            pos_y = random.randint(-250, 250)
            car.goto(280, pos_y)
    

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT

