from algorithm_old import Algorithm

attraction_number = 6

a = Algorithm(attraction_number, 0.3, 1, 1, 1000, 0.1, 0.3)

print(a.ant.pheromone_traces)
print(a.ant.attraction_distance)
