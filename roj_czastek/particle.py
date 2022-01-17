import math


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

    def calculate_adaptation(self):
        return self.function(self.x, self.y)

    def update_adaptation(self):
        self.adaptation = self.calculate_adaptation()
        if self.adaptation < self.best_adaptation:
            self.best_adaptation = self.adaptation
            self.best_x = self.x
            self.best_y = self.y
