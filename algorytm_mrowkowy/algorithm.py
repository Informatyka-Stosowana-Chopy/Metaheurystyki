from ant import Ant


class Algorithm:
    def __init__(self, attractions_number: int, multiplier: float, attraction_distance: list):
        self.pheromone_traces = [
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ]
        self.attractions_number = attractions_number
        self.multiplier = multiplier

        self.ant_colony = []
        self.configure_ants()

        self.attraction_distance = attraction_distance

    def configure_ants(self):
        ants_number = round(self.attractions_number * self.multiplier)
        for _ in range(0, ants_number):
            self.ant_colony.append(Ant(self.attractions_number, self.attraction_distance))

