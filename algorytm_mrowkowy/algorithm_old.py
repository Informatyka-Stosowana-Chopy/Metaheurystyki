import ant_old
from ant_old import Ant


class Algorithm:
    def __init__(self, attraction_number: int, choice_probability: float, pheromone_weight: float,
                 heuristics_weight: float, iter_number: int, evaporation_ratio: float, multiplier: float):
        self.ant = Ant(attraction_number)
        self.pheromone_weight = pheromone_weight
        self.heuristics_weight = heuristics_weight
        self.choice_probability = choice_probability
        self.iter_number = iter_number
        self.evaporation_ratio = evaporation_ratio
        self.multiplier = multiplier

    def pheromones_update(self, multiplier):
        for x in range(0, self.ant.attractions_number):
            for y in range(0, self.ant.attractions_number):
                self.ant.pheromone_traces[x][y] = self.ant.pheromone_traces[x][y] * self.evaporation_ratio
                for ant.Ant in self.ant.configure_ants(multiplier):
                    self.ant.pheromone_traces[x][y] += 1/self.ant.get_total_distance()

    def get_best(self, previous_best_ant: Ant):
        best_ant = previous_best_ant
        for ant.Ant in self.ant.configure_ants(self.multiplier):
            travelled_distance = self.ant.get_total_distance()
            if travelled_distance < best_ant.get_total_distance():
                best_ant = ant
        return best_ant

    def solve(self): # TODO
        self.pheromones_update(self.multiplier)
        #self.get_best(ant: Ant) = None # TODO
        for i in range(0, self.iter_number):
            self.ant.configure_ants(self.multiplier)
            for r in range(0, self.ant.attractions_number - 1):
                pass
                #self.ant.probabilistic_attraction_visit() # TODO
            self.pheromones_update(self.multiplier)






