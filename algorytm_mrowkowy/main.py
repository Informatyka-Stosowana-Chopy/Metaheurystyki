from algorithm import Algorithm

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

algorithm = Algorithm(ants[0], evaporation[0], 4, alpha[0], beta[0], random_attraction, "A-n32-k5.txt")
#print(algorithm.ant_colony[0].attraction_distance)
algorithm.solve()
print(algorithm.best_ant.get_total_distance())
print(algorithm.best_ant.visited_attractions)
print(set(algorithm.best_ant.visited_attractions))
