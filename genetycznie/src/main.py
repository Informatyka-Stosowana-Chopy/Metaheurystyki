from algorithm import Algorithm

BACKPACK_MAX_CAPACITY = 6_404_180

p = Algorithm(backpack_max_capacity=BACKPACK_MAX_CAPACITY, population_size=10, individual_size=26,
              generation_numbers=100, iter=0, children=[])

p.simulation()

print("############")
print("wartość:", p.get_the_best_individual().fitness)
print("Liczba iteracji: ", p.iter)
print("Wielkość populacji: ", p.population_size)
print("Prawdopodobieństwo mutacji: ", len(p.children) / len(p.population) * 100, " %")
print("Prawdopodobieństwo krzyżowania: ", p.get_probability_in_population(), " %")
