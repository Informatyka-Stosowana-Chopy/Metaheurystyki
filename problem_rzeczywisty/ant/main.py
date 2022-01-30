from algorithm import Algorithm

#####################################
# CONSTANT
#####################################
ants = [10, 30, 50]
random_attraction = 0.3
alpha = [1, 2]
beta = [1, 3]
iteration = 10
evaporation = [0.1, 0.5]
#####################################
# MAINv
#####################################

algorithm = Algorithm(ants[0], evaporation[0], 4, alpha[0], beta[0], random_attraction, "data.txt")
algorithm.solve()
print(algorithm.best_ant.get_total_distance())
print(algorithm.best_ant.visited_attractions)
print(set(algorithm.best_ant.visited_attractions))
