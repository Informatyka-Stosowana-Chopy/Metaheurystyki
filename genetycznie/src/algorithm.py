import random
from copy import copy

from backpack import Backpack
from individual import Individual


class Algorithm:
    def __init__(self, backpack_max_capacity: int, population_size: int, individual_size: int, generation_numbers: int,
                 iter: int, children):
        self.backpack = Backpack(backpack_max_capacity)
        self.population_size = population_size
        self.individual_size = individual_size
        self.generation_numbers = generation_numbers
        self.iter = iter
        self.children = children
        self.population = self.__generate_initial_population()

    def __generate_initial_population(self):
        population = []
        for individual in range(self.population_size):
            current_individual = Individual(self.individual_size)
            for gen in range(self.individual_size):
                random_gen = random.randint(0, 1)  # generate value 0 or 1
                current_individual.gens.append(random_gen)
            population.append(current_individual)
        return population

    def __calculate_fitness_of_the_individual(self, individual: Individual):
        sum_of_weight = 0.0
        sum_of_values = 0.0
        for i, gen in enumerate(individual.gens):
            if gen == 1:
                sum_of_weight += self.backpack.items['Waga'][i]
                sum_of_values += self.backpack.items['Wartosc'][i]
            if sum_of_weight > self.backpack.max_capacity:
                individual.fitness = 0
                return 0

        individual.fitness = sum_of_values
        return sum_of_values  # fitness of the individual

    def __calculate_fitness_of_population(self):
        for individual in self.population:
            self.__calculate_fitness_of_the_individual(individual)

    def __set_probability_in_population(self):
        sum_of_fitness = 0
        for individual in self.population:
            sum_of_fitness += individual.fitness

        for individual in self.population:
            try:
                individual.choose_probability = individual.fitness / sum_of_fitness
            except ZeroDivisionError:
                individual.choose_probability = 0

    def get_probability_in_population(self):
        sum_probability = 0
        for individual in self.population:
            if individual.choose_probability is not None:
                sum_probability += individual.choose_probability
        return sum_probability * 100

    def roulette_wheel_selection(self, number_of_chosen):
        self.__set_probability_in_population()
        intervals = []
        sum_ = 0

        for i in range(number_of_chosen):
            intervals.append([i, sum_, sum_ + self.population[i].choose_probability])
            sum_ += self.population[i].choose_probability

        random_number = random.random()
        result = [interval for interval in intervals if interval[1] < random_number <= interval[2]]
        return result

    def one_point_crossing(self, parent_a: Individual, parent_b: Individual, crossing_point):
        children = []
        children_1 = Individual(self.individual_size)
        children_2 = Individual(self.individual_size)
        for i, gen in enumerate(parent_a.gens):
            if i <= crossing_point:
                children_1.gens.append(copy(parent_a.gens[i]))
            else:
                children_1.gens.append(copy(parent_b.gens[i]))

        for i, gen in enumerate(parent_a.gens):
            if i <= crossing_point:
                children_2.gens.append(copy(parent_b.gens[i]))
            else:
                children_2.gens.append(copy(parent_a.gens[i]))

        children.append(children_1)
        children.append(children_2)

        return children

    def individual_mutation(self, individual: Individual):
        random_gen = random.randint(0, self.individual_size - 1)
        if individual.gens[random_gen] == 1:
            individual.gens[random_gen] = 0
        else:
            individual.gens[random_gen] = 1
        return individual

    def connect_population_and_children(self, child: Individual):
        self.population.append(child)
        self.population_size += 1

    def delete_weak_individual(self):
        for individual in self.population:
            if individual.fitness == 0:
                self.population.remove(individual)
                self.population_size -= 1

    def simulation(self):
        the_best_global_adaptation = 0
        for generation in range(self.generation_numbers):
            the_best_current_adaptation = 0
            self.delete_weak_individual()
            self.__calculate_fitness_of_population()
            for individual in self.population:
                if individual.fitness > the_best_current_adaptation:
                    the_best_current_adaptation = individual.fitness
                    self.iter += 1

            if the_best_current_adaptation > the_best_global_adaptation:
                the_best_global_adaptation = the_best_current_adaptation

            parent_1 = self.roulette_wheel_selection(self.population_size)
            parent_2 = self.roulette_wheel_selection(self.population_size)

            crossing_point = random.randint(0, self.individual_size - 1)
            self.children = self.one_point_crossing(self.population[parent_1[0][0]],
                                                    self.population[parent_2[0][0]], crossing_point)

            for child in self.children:
                child = self.individual_mutation(child)
                self.connect_population_and_children(child)

    def get_the_best_individual(self):
        global_max = 0
        best_index = 0
        for i, individual in enumerate(self.population):
            if individual.fitness > global_max:
                global_max = individual.fitness
                best_index = i
        return self.population[best_index]
