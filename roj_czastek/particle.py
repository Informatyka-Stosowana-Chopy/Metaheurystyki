import math
import random


class Particle:
    def __init__(self, x, y, inersion, cognitive_constant, social_constant, function):
        self.x = x
        self.y = y
        self.inersion = inersion
        self.cognitive_constant = cognitive_constant
        self.social_constant = social_constant
        self.function = function

        self.adaptation = math.inf
        self.speed = 0
        self.best_x = x
        self.best_y = y
        self.best_adaptation = math.inf

    def __calculate_adaptation(self):
        return self.function(self.x, self.y)

    def update_adaptation(self):
        self.adaptation = self.__calculate_adaptation()
        if self.adaptation < self.best_adaptation:
            self.best_adaptation = self.adaptation
            self.best_x = self.x
            self.best_y = self.y

    def __calculate_new_speed(self):
        iteration_component = self.inersion * self.speed
        cognitive_component = self.cognitive_constant * random.uniform(0, 1)
        cognitive_component *= (math.sqrt(pow(self.best_x - self.x, 2) + pow(self.best_y - self.y, 2)))
        social_component = self.social_constant * random.uniform(0, 1)
        social_component *= (math.sqrt(pow(self.best_x - self.x, 2) + pow(self.best_y - self.y, 2)))
        self.speed = iteration_component + cognitive_component + social_component

    def update_coordinates(self):
        self.__calculate_new_speed()
        self.x += self.speed
        self.y += self.speed
