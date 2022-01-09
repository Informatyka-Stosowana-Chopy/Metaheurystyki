import random


class Ant:
    def __init__(self, attractions_number: int, attraction_distance: list):
        self.attractions_number = attractions_number
        self.visited_attractions = []
        self.visited_attractions.append(random.randint(0, self.attractions_number - 1))
        self.visited_attractions = []

        self.attraction_distance = attraction_distance
        # TODO zrobić by było wczytywane z pliku i aktualizowane - w mainie albo osobnej klasie (lepiej w klasie)

    def visit_(self):
        pass

    def visit_attraction(self):
        pass

    def visit_random_attraction(self):
        pass

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

    def visit_attractions_probabilistically(self, pheromone_traces, alfa, beta):
        current_attraction = self.visited_attractions[-1]
        all_attractions = [_ for _ in range(0, self.attractions_number)]
        available_attractions = [attraction for attraction in all_attractions if attraction not in self.visited_attractions]

        using_index = []
        using_probability = []
        probability_sum = 0

        for attraction in available_attractions:
            using_index.append(attraction)
            pheromone = pow(pheromone_traces[current_attraction][attraction], alfa)
            heuristic = pow(1/self.attraction_distance[current_attraction][attraction], beta)
            probability = pheromone * heuristic
            using_probability.append(probability)
        using_probability = [probability / probability_sum for probability in using_probability]  # TODO to chyba źle
        return [using_index, using_probability]








