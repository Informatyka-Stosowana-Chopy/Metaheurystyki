import timeit


def readFileTo2DArray(fileName):
    with open(fileName + '.txt') as f:
        contents = f.read()

    counter = 0
    tmp = ''
    matrix = [[]]
    for char in contents:
        if char == '\n':
            matrix.append([])
            if tmp != '':
                matrix[counter].append(int(tmp))
            else:
                matrix[counter].append(0)
            tmp = ''
            counter += 1
        elif char == ' ':
            matrix[counter].append(int(tmp))
            tmp = ''
        else:
            tmp += char
    if tmp != '':
        matrix[counter].append(int(tmp))
    else:
        matrix[counter].append(0)
    return matrix


def bfsLista(graph, start, end):
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


def bfsMacierz(graph, start, end):
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


def bfsTablica(graph, start, end):
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


def dfsLista(graph, start, end):
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


def dfsMacierz(graph, start, end):
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


def dfsTablica(graph, start, end):
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


def test(graph, start, end, number, bfs, dfs):
    avgTime = 0
    result = "BFS\nSciezka " + str(bfs(graph, start, end)) + "\n"
    result += "Dlugosc sciezki " + str(len(bfs(graph, start, end))) + "\n"
    for i in range(number):
        tmp = '{0:.4e}'.format(timeit.timeit("bfs(graph, start, end)", globals=locals(), number=1))
        avgTime += float(tmp)
        result += str(tmp) + " s\n"
    avgTime /= number
    result += "Srednia czasu " + str('{0:.4e}'.format(avgTime)) + " s\n"

    avgTime = 0
    result += "DFS\nSciezka " + str(dfs(graph, start, end)) + "\n"
    result += "Dlugosc sciezki " + str(len(dfs(graph, start, end))) + "\n"
    for i in range(number):
        tmp = '{0:.4e}'.format(timeit.timeit("dfs(graph, start, end)", globals=locals(), number=1))
        avgTime += float(tmp)
        result += str(tmp) + " s\n"
    avgTime /= number
    result += "Srednia czasu " + str('{0:.4e}'.format(avgTime)) + " s\n"

    return result


choice = 1
while (choice != 0):
    choice = int(input("[1] Generuj\n[2] Zaczytaj z pliku\n[0] Wyjscie\n"))
    if choice == 1:
        number = int(input("Ile wykonan kazdego algorytmu\n"))
        nodes = int(input("Ile wezlow?\n"))
        start = int(input("Podaj wezel poczatkowy\n"))
        end = int(input("Podaj wezel koncowy\n"))

        macierzIncydencji = readFileTo2DArray("data/macierzIncydencji.txt")
        macierzSasiedztwa = readFileTo2DArray("data/macierzIncydencji.txt")
        tablicaN = readFileTo2DArray("data/macierzIncydencji.txt")
        tablicaS = readFileTo2DArray("data/macierzIncydencji.txt")
        listaSasiedztwaN = readFileTo2DArray("data/macierzIncydencji.txt")
        listaSasiedztwaS = readFileTo2DArray("data/macierzIncydencji.txt")

        print("###################################################################")
        print("Macierz sasiedztwa")
        print(test(macierzSasiedztwa, start, end, number, bfsMacierz, dfsMacierz))
        print("###################################################################")
        print("Macierz incydencji")
        print(test(macierzIncydencji, start, end, number, bfsMacierz, dfsMacierz))
        print("###################################################################")
        print("Lista sasiedztwa nieskierowana")
        print(test(listaSasiedztwaN, start, end, number, bfsLista, dfsLista))
        print("###################################################################")
        print("Lista sasiedztwa skierowana")
        print(test(listaSasiedztwaS, start, end, number, bfsLista, dfsLista))
        print("###################################################################")
        print("Tablica nieskierowana")
        print(test(tablicaN, start, end, number, bfsTablica, dfsTablica))
        print("###################################################################")
        print("Tablica skierowana")
        print(test(tablicaS, start, end, number, bfsTablica, dfsTablica))
        print("###################################################################")
    elif choice == 2:
        choice2 = int(input(
            "[1] Macierz incydencji\n[2] Macierz sasiedztwa\n[3] Lista sasiedztwa skierowana\n[4] Lista sasiedztwa nieskierowana\n[5] Tablica skierowana\n[6] Tablica nieskierowana\n"))
        filename = input("Podaj nazwe pliku tekstowego\n")
        number = int(input("Ile wykonan kazdego algorytmu\n"))
        start = int(input("Podaj wezel poczatkowy\n"))
        end = int(input("Podaj wezel koncowy\n"))
        if choice2 == 1:
            macierzIncydencji = readFileTo2DArray(filename)
            print(test(macierzIncydencji, start, end, number, bfsMacierz, dfsMacierz))
        if choice2 == 2:
            macierzSasiedztwa = readFileTo2DArray(filename)
            print(test(macierzSasiedztwa, start, end, number, bfsMacierz, dfsMacierz))
        if choice2 == 3:
            listaSasiedztwaS = readFileTo2DArray(filename)
            print(test(listaSasiedztwaS, start, end, number, bfsLista, dfsLista))
        if choice2 == 4:
            listaSasiedztwaN = readFileTo2DArray(filename)
            print(test(listaSasiedztwaN, start, end, number, bfsLista, dfsLista))
        if choice2 == 5:
            tablicaS = readFileTo2DArray(filename)
            print(test(tablicaS, start, end, number, bfsTablica, dfsTablica))
        if choice2 == 6:
            tablicaN = readFileTo2DArray(filename)
            print(test(tablicaN, start, end, number, bfsTablica, dfsTablica))

########### GRAFY ZACZYTYWANE Z PLIKU  DO SPRAWKA###############
# number = 5
# start = 1
# end = 4
# start2 = 1
# end2 = 20

# macierzSasiedztwa5 = readFileTo2DArray('macierzSasiedztwa')
# macierzIncydencji5 = readFileTo2DArray('macierzIncydencji')
# listaSasiedztwaN5 = readFileTo2DArray('listaSasiedztwaN')
# listaSasiedztwaS5 = readFileTo2DArray('listaSasiedztwaS')
# tablicaN5 = readFileTo2DArray('tablicaN')
# tablicaS5 = readFileTo2DArray('tablicaS')
# macierzSasiedztwa25 = readFileTo2DArray('macierzSasiedztwa25')
# macierzIncydencji25 = readFileTo2DArray('macierzIncydencji25')
# listaSasiedztwaN25 = readFileTo2DArray('listaSasiedztwaN25')
# listaSasiedztwaS25 = readFileTo2DArray('listaSasiedztwaS25')
# tablicaN25 = readFileTo2DArray('tablicaN25')
# tablicaS25 = readFileTo2DArray('tablicaS25')

# print("###################################################################")
# print("GRAF 5 WEZLOW")
# print("Macierz sasiedztwa")
# print(test(macierzSasiedztwa5, start, end, number, bfsMacierz, dfsMacierz))
# print("###################################################################")
# print("Macierz incydencji")
# print(test(macierzIncydencji5, start, end, number, bfsMacierz, dfsMacierz))
# print("###################################################################")
# print("Lista sasiedztwa nieskierowana")
# print(test(listaSasiedztwaN5, start, end, number, bfsLista, dfsLista))
# print("###################################################################")
# print("Lista sasiedztwa skierowana")
# print(test(listaSasiedztwaS5, start, end, number, bfsLista, dfsLista))
# print("###################################################################")
# print("Tablica nieskierowana")
# print(test(tablicaN5, start, end, number, bfsTablica, dfsTablica))
# print("###################################################################")
# print("Tablica skierowana")
# print(test(tablicaS5, start, end, number, bfsTablica, dfsTablica))
# print("###################################################################")
# print("###################################################################")
# print("GRAF 25 WEZLOW")
# print("Macierz sasiedztwa")
# print(test(macierzSasiedztwa25, start2, end2, number, bfsMacierz, dfsMacierz))
# print("###################################################################")
# print("Macierz incydencji")
# print(test(macierzIncydencji25, start2, end2, number, bfsMacierz, dfsMacierz))
# print("###################################################################")
# print("Lista sasiedztwa nieskierowana")
# print(test(listaSasiedztwaN25, start2, end2, number, bfsLista, dfsLista))
# print("###################################################################")
# print("Lista sasiedztwa skierowana")
# print(test(listaSasiedztwaS25, start2, end2, number, bfsLista, dfsLista))
# print("###################################################################")
# print("Tablica nieskierowana")
# print(test(tablicaN25, start2, end2, number, bfsTablica, dfsTablica))
# print("###################################################################")
# print("Tablica skierowana")
# print(test(tablicaS25, start2, end2, number, bfsTablica, dfsTablica))
# print("###################################################################")
