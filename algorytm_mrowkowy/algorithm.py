import random
import matplotlib.pyplot as plt

from ant import Ant
from attraction import Attraction
import math


class Algorithm:
    def __init__(self, multiplier: float, evaporation: float,
                 iteration_number: int, alfa: int, beta: int, probability_random_attraction: float, file_name: str):
        self.pheromone_traces = []
        self.file_name = file_name
        self.probability_random_attraction = probability_random_attraction
        self.attractions_number = 0
        self.multiplier = multiplier
        self.iteration_number = iteration_number
        self.attraction_distance = []
        self.all_attraction = []

        self.__read_attraction()

        self.ant_colony = []
        self.configure_ants()
        self.best_ant: Ant = None

        self.evaporation = evaporation  # <0, 1>

        self.alfa = alfa
        self.beta = beta

    def __read_attraction(self):
        # TODO update pheromone traces
        with open(f"data/{self.file_name}", "r") as file:
            for line in file:
                line = line.split(sep=" ")
                # line[1] - index, line[2] - x, line[3] - y
                self.all_attraction.append(Attraction(int(line[1]), int(line[2]), int(line[3])))
        self.attractions_number = len(self.all_attraction)

        # update pheromone traces
        help_lista = []
        for _ in range(self.attractions_number):
            help_lista.append(1)
        for i in range(self.attractions_number):
            self.pheromone_traces.append(help_lista)

        # prepare attraction distance list
        for attraction_x in self.all_attraction:
            help_array = []
            for attraction_y in self.all_attraction:
                help_array.append(math.sqrt(pow(attraction_x.x - attraction_y.x, 2) + pow(attraction_y.y - attraction_x.y, 2)))
            self.attraction_distance.append(help_array)

    def configure_ants(self):
        ants_number = round(self.multiplier)  # TODO na sztywno jak w zadaniu
        self.ant_colony = []
        for _ in range(0, ants_number):
            self.ant_colony.append(Ant(self.attractions_number, self.attraction_distance, self.all_attraction))

    def update_pheromone(self):
        for x in range(0, self.attractions_number):
            for y in range(0, self.attractions_number):
                self.pheromone_traces[x][y] = self.pheromone_traces[x][y] * self.evaporation
                for ant in self.ant_colony:
                    self.pheromone_traces[x][y] += 1 / ant.get_total_distance()

    def get_best_ant(self):
        for ant in self.ant_colony:
            total_distance = ant.get_total_distance()
            if total_distance < self.best_ant.get_total_distance():
                self.best_ant = ant

    def solve(self):
        for i in range(0, self.iteration_number):
            self.configure_ants()
            for r in range(0, self.attractions_number - 1):
                for ant in self.ant_colony:
                    # select attraction
                    method = random.uniform(0, 1)
                    if method <= self.probability_random_attraction:
                        ant.visit_random_attraction()
                    else:
                        index_to_visit = ant.roulette_selection(self.pheromone_traces, self.alfa, self.beta)[0][0]
                        ant.visit_attraction(index_to_visit)
                    ant.current_distance = ant.get_total_distance()
                    if r == 0:
                        self.best_ant = self.ant_colony[0]
            self.update_pheromone()
            self.get_best_ant()
        self.make_chart()

    def make_chart(self):
        # prepare data
        x_val = []
        y_val = []
        for attraction in self.best_ant.visited_attractions:
            x_val.append(self.all_attraction[attraction].x)
            y_val.append(self.all_attraction[attraction].y)

        plt.plot(x_val, y_val, '-o')
        plt.show()
