class Individual:
    def __init__(self, individual_size: int):
        self.individual_size = individual_size
        self.gens = []
        self.choose_probability = None
        self.fitness = 0
