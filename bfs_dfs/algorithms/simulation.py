from reader import Reader
import timeit


class Simulation:
    def __init__(self):
        self.graph = Reader()

    def bfs_lista(self, graph, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for x in graph[int(node) - 1]:
                new_path = list(path)
                new_path.append(x)
                queue.append(new_path)

    def bfs_macierz(self, graph, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for x in range(len(graph[int(node) - 1])):
                if graph[int(node) - 1][x] == 1:
                    new_path = list(path)
                    new_path.append(x + 1)
                    queue.append(new_path)

    def bfs_tablica(self, graph, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for x in graph:
                if x[0] == node:
                    new_path = list(path)
                    new_path.append(x[1])
                    queue.append(new_path)

    def dfs_lista(self, graph, start, end):
        stack = [(start, [start])]
        visited = set()
        while stack:
            (node, path) = stack.pop()
            if node not in visited:
                if node == end:
                    return path
                visited.add(node)
                for x in graph[node - 1]:
                    stack.append((x, path + [x]))

    def dfs_macierz(self, graph, start, end):
        stack = [(start, [start])]
        visited = set()
        while stack:
            (node, path) = stack.pop()
            if node not in visited:
                if node == end:
                    return path
                visited.add(node)
                for x in range(len(graph[node - 1])):
                    if graph[node - 1][x] == 1:
                        stack.append((x + 1, path + [x + 1]))

    def dfs_tablica(self, graph, start, end):
        stack = [(start, [start])]
        visited = set()
        while stack:
            (node, path) = stack.pop()
            if node not in visited:
                if node == end:
                    return path
                visited.add(node)
                for x in graph:
                    if x[0] == node:
                        stack.append((x[1], path + [x[1]]))

    @staticmethod
    def __simulate(graph: list, start: int, end: int, number_of_repetitions: int, bfs_algorithm, dfs_algorithm):
        average_time = 0
        result = f"\n{bfs_algorithm.__name__}:\nŚcieżka: " + str(bfs_algorithm(graph, start, end)) + "\n"
        result += "Długość ścieżki: " + str(len(bfs_algorithm(graph, start, end))) + "\n"

        for i in range(number_of_repetitions):
            tmp = '{0:.4e}'.format(timeit.timeit("bfs_algorithm(graph, start, end)", globals=locals(), number=1))
            average_time += float(tmp)
            result += str(tmp) + " s\n"
        average_time /= number_of_repetitions
        result += "Średni czas: " + str('{0:.4e}'.format(average_time)) + " s\n\n"

        average_time = 0
        result += f"{dfs_algorithm.__name__}:\nŚcieżka: " + str(dfs_algorithm(graph, start, end)) + "\n"
        result += "Długość ścieżki: " + str(len(dfs_algorithm(graph, start, end))) + "\n"

        for i in range(number_of_repetitions):
            tmp = '{0:.4e}'.format(timeit.timeit("dfs_algorithm(graph, start, end)", globals=locals(), number=1))
            average_time += float(tmp)
            result += str(tmp) + " s\n"
        average_time /= number_of_repetitions
        result += "Średni czas: " + str('{0:.4e}'.format(average_time)) + " s\n"
        result += "\n#############################################"

        return result

    def main(self):
        # TODO może trzeba zrobić wybór by dla każdego algorytmu coś innego podać
        number = int(input("Ilosc powtórzeń każdego algorytmu: "))
        start = int(input("Węzeł początkowy:"))
        end = int(input("Węzeł końcowy: "))

        print(self.__simulate(self.graph.macierzIncydencji, start, end, number, self.bfs_macierz, self.dfs_macierz))

        print(self.__simulate(self.graph.macierzSasiedztwa, start, end, number, self.bfs_macierz, self.dfs_macierz))

        print(self.__simulate(self.graph.listaSasiedztwaS, start, end, number, self.bfs_lista, self.dfs_lista))

        print(self.__simulate(self.graph.listaSasiedztwaN, start, end, number, self.bfs_lista, self.dfs_lista))

        print(self.__simulate(self.graph.tablicaS, start, end, number, self.bfs_tablica, self.dfs_tablica))

        print(self.__simulate(self.graph.tablicaN, start, end, number, self.bfs_tablica, self.dfs_tablica))
