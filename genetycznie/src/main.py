from algorithm import Algorithm
BACKPACK_MAX_CAPACITY = 6_404_180

p = Algorithm(BACKPACK_MAX_CAPACITY, 10, 26, 1000)
p.simulation()

local_max = 0
for individual in p.population:
    if individual.fitness > local_max:
        local_max = individual.fitness
    print(individual.fitness)

print("############")
print(local_max)
