from algorithm import Algorithm
import math


###############################
# MATH FUNCTION
###############################
def booth_function(x, y):
    return pow(x + 2 * y - 7, 2) + pow(2 * x + y - 5, 2)


def matyas_function(x, y):
    return 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y


###############################
# CONSTANT
###############################
# TODO change it to some other numbers to check if it has influence
inersion = 0.2
cognitive_constant = 0.35
social_constant = 0.45
iteration = 100
number_of_particle = 100
###############################
# MAIN
###############################

a = Algorithm(number_of_particle, inersion, cognitive_constant, social_constant, iteration, matyas_function)
a.find_local_minimum()
print(a.best_particle.best_x, a.best_particle.best_y)
