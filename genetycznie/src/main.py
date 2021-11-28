from algorithm import Algorithm

BACKPACK_MAX_CAPACITY = 6_404_180

p = Algorithm(backpack_max_capacity=BACKPACK_MAX_CAPACITY, population_size=10, individual_size=26,
              generation_numbers=100)

p.simulation()

print("############")
print("wartość:", p.get_the_best_individual().fitness)
