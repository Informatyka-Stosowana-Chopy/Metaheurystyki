import random

from backpack import Backpack
from individual import Individual


class Algorithm:
    def __init__(self, backpack_max_capacity: int, population_size: int, individual_size: int):
        self.backpack = Backpack(backpack_max_capacity)
        self.population_size = population_size
        self.individual_size = individual_size
        self.population = self.generate_initial_population()

    def generate_initial_population(self):
        population = []
        for individual in range(self.population_size):
            current_individual = Individual(self.individual_size)
            for gen in range(self.individual_size):
                random_gen = random.randrange(0, 2)  # generate value 0 or 1
                current_individual.gens.append(random_gen)
            population.append(current_individual)
        return population

    def calculate_fitness_of_the_individual(self, individual):
        sum_of_weight = 0
        sum_of_values = 0
        for i, gen in enumerate(individual):
            if individual.gens[i] == 1:
                sum_of_weight += self.backpack.items['Waga'][i]
                sum_of_values += self.backpack.items['Wartosc'][i]
            if sum_of_weight > self.backpack.max_capacity:
                return 0

        individual.fitness = sum_of_values
        return sum_of_values  # fitness of the individual

    def set_probability_in_population(self):
        sum_of_fitness = 0
        for individual in self.population:
            sum_of_fitness += self.calculate_fitness_of_the_individual(individual)

        for individual in self.population:
            individual.choose_probability = individual.fitness / sum_of_fitness

    def roulette_wheel_selection(self, number_of_chosen):
        self.set_probability_in_population()
        intervals = []
        suma = 0

        for i in range(number_of_chosen):
            intervals.append([i, suma, suma + self.population[i].choose_probability])  # TODO check if [2] is float
            suma += self.population[i].choose_probability

        random_number = random.random()
        result = [interval for interval in intervals if interval[1] < random_number <= interval[2]]
        return result
