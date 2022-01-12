from algorithm import Algorithm

attraction_distance = [
    [0, 8, 7, 4, 6, 4],
    [8, 0, 5, 7, 11, 5],
    [7, 5, 0, 9, 6, 7],
    [4, 7, 9, 0, 5, 6],
    [6, 11, 6, 5, 0, 3],
    [4, 5, 7, 6, 3, 0]
]

#####################################
# CONSTANT
#####################################
attraction_number = 6
ants = [10, 30, 50]
random_attraction = 0.3
alpha = [1, 2]
beta = [1, 3]
iteration = 1000
evaporation = [0.1, 0.5]
#####################################
# MAINv
#####################################

algorithm = Algorithm(ants[0], evaporation[0], 1, alpha[0], beta[0], random_attraction, "A-n32-k5.txt")
algorithm.solve()
print(algorithm.best_ant.get_total_distance())
print(algorithm.best_ant.visited_attractions)
