import random


class Ant:
    def __init__(self, attractions_number: int):
        self.total_attractions = random.randint(0, attractions_number)
        self.used_probability = []
        self.used_indexes = []
        self.visited_attractions = []
        self.visited_attractions.append(random.randint(0, attractions_number - 1))
        self.available_attractions = self.total_attractions - self.visited_attractions[0]
        self.attractions_number = attractions_number

        self.attraction_distance = [
            [0, 8, 7, 4, 6, 4],
            [8, 0, 5, 7, 11, 5],
            [7, 5, 0, 9, 6, 7],
            [4, 7, 9, 0, 5, 6],
            [6, 11, 6, 5, 0, 3],
            [4, 5, 7, 6, 3, 0]
        ]
        self.pheromone_traces = [
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ]

    def visit_attraction(self):
        pass

    def visit_random_attraction(self):
        pass

    def probabilistic_attraction_visit(self, alfa, beta):
        current_attraction = self.visited_attractions[-1]
        probability_sum = 0

        for attraction in range(self.available_attractions):
            self.used_indexes.append(attraction)
            pheromones = pow(self.pheromone_traces[current_attraction][attraction], alfa)
            heuristic = pow(self.attraction_distance[current_attraction][attraction], beta)
            probability = pheromones * heuristic

            self.used_probability.append(probability)

        for probability in self.used_probability:
            self.used_probability = [probability / probability_sum]

        return [self.used_indexes, self.used_probability]

    def roulette_selection(self):
        intervals = []
        total = 0

        for i in range(0, self.available_attractions):
            total += self.used_probability[i]
            intervals.append(self.used_indexes[i])

        random_number = random.uniform(0, 1)
        result = 0.0
        for interval in intervals:
            if interval[1] < random_number <= interval[2]:
                result = random_number
        return result

    def get_total_distance(self):
        total_distance = 0
        for a in range(1, len(self.visited_attractions)):
            total_distance += abs(self.visited_attractions[a - 1] - self.visited_attractions[a])

        return total_distance

    def configure_ants(self, multiplier: float):  # TODO: nie wiem czy powinno byc to tutaj czy w klasie algorithm
        ants_number = round(self.attractions_number * multiplier)
        ant_colony = []
        for i in range(0, ants_number):
            ant_colony.append(self)
        return ant_colony
