import random

import pandas as pd

from reader import Reader


class Backpack:
    def __init__(self, max_capacity: int):
        self.max_capacity = max_capacity
        self.items = []
        self.all_available_items = Reader.read_csv()

    def generate_initial_population(self, population_size, individual_size):
        population = []
        for individual in range(population_size):
            current_individual = []
            for gen in range(individual_size):
                random_gen = random.randrange(0, 2)  # generate value 0 or 1
                current_individual.append(random_gen)
            population.append(current_individual)
        return population

    def calculate_fitness_of_the_individual(self, individual, backpack_items, max_backpack_capacity):
        sum_of_weight = 0
        sum_of_values = 0
        for i, gen in enumerate(individual):
            current_bit = gen
            if current_bit == 1:
                sum_of_weight += backpack_items[i]['Waga']  # TODO check if it is in good order
                sum_of_values += backpack_items[i]['Wartosc']
            if sum_of_weight > max_backpack_capacity:
                return 0
        return sum_of_values  # fitness of the individual

    def roulette_wheel_selection(self):
        pass
