import random
import math


class Ant:
    def __init__(self, attractions_number: int, attraction_distance: list, all_attraction: list):
        self.available_attractions = None
        self.attractions_number = attractions_number
        self.all_attractions = all_attraction
        self.visited_attractions = []
        self.visited_attractions.append(random.randint(0, self.attractions_number - 1))

        self.using_index = []
        self.using_probability = []

        self.attraction_distance = attraction_distance
        self.current_distance = 0
        # TODO zrobić by było wczytywane z pliku i aktualizowane - w mainie albo osobnej klasie (lepiej w klasie)

    def visit_attraction(self, attraction_index: int):
        self.visited_attractions.append(attraction_index)
        self.__update_available_attractions()

    def visit_random_attraction(self):
        self.__update_available_attractions()

        self.visited_attractions.append(
            self.available_attractions[random.randint(0, len(self.available_attractions) - 1)].index)

        self.__update_available_attractions()

    def __update_available_attractions(self):
        self.available_attractions = [attraction for attraction in self.all_attractions if
                                      attraction.index not in self.visited_attractions]

    def roulette_selection(self, pheromone_traces, alfa, beta):
        intervals = []
        total = 0
        self.visit_attractions_probabilistically(pheromone_traces, alfa, beta)
        for i in range(0, len(self.available_attractions)):
            intervals.append([self.using_index[i], total, total + self.using_probability[i]])
            total += self.using_probability[i]

        random_number = random.uniform(0, 1)
        result = [interval for interval in intervals if interval[1] < random_number <= interval[2]]
        return result

    def get_total_distance(self):
        total_distance = 0
        for a in range(1, len(self.visited_attractions)):
            total_distance += math.sqrt(pow(
                self.all_attractions[self.visited_attractions[a - 1]].x - self.all_attractions[
                    self.visited_attractions[a]].x, 2) + pow(
                self.all_attractions[self.visited_attractions[a - 1]].y - self.all_attractions[
                    self.visited_attractions[a]].y, 2))

        return total_distance

    def visit_attractions_probabilistically(self, pheromone_traces, alfa, beta):
        current_attraction = self.visited_attractions[-1]
        self.__update_available_attractions()

        probability_sum = 0
        using_probability = []
        self.using_index = []
        self.using_probability = []
        for attraction in self.available_attractions:
            self.using_index.append(attraction.index)
            pheromone = pow(pheromone_traces[current_attraction][attraction.index], alfa)
            heuristic = pow(1 / self.attraction_distance[current_attraction][attraction.index], beta)
            probability = pheromone * heuristic
            using_probability.append(probability)
            probability_sum += probability
        self.using_probability = [probability / probability_sum for probability in
                                  using_probability]
