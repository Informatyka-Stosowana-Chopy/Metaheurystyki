from algorithm import Algorithm
def f(x, y):
    return x ** 2


a = Algorithm(10, f)
a.calculate_adaptation(4,6)
