class Attraction:
    def __init__(self, index: int, x: float, y: float, demand: float, ready_time: float, due_time: float, service_time:float):
        self.index = index - 1
        self.x = x
        self.y = y
        self.demand = demand
        self.ready_time = ready_time
        self.due_time = due_time
        self.service_time = service_time

