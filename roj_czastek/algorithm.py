from particle import Particle
import random
import math


class Algorithm:
    def __init__(self, population_size: int, inersion, cognitive_constant, social_constant,  iteration, function):
        self.social_constant = social_constant
        self.cognitive_constant = cognitive_constant
        self.inersion = inersion
        self.population_size = population_size
        self.function = function
        self.population = []
        self.generate_population()
        self.iteration = iteration
        self.best_particle = None

    def generate_population(self):
        for particle in range(self.population_size):
            self.population.append(
                Particle(random.uniform(-10, 10), random.uniform(-10, 10), self.inersion, self.cognitive_constant,
                         self.social_constant, self.function))

    def get_best(self):
        best_adaptation = math.inf
        for particle in self.population:
            particle.update_adaptation()
            if particle.best_adaptation < best_adaptation:
                best_adaptation = particle.best_adaptation
                self.best_particle = particle

    def find_local_minimum(self):
        for i in range(self.iteration):
            self.get_best()
            for particle in self.population:
                particle.update_coordinates()

