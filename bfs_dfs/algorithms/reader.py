import os


class Reader:
    def __init__(self):
        self.macierzIncydencji = self.read_file("macierzIncydencji.txt")
        self.macierzSasiedztwa = self.read_file("macierzSasiedztwa.txt")
        self.listaSasiedztwaS = self.read_file("listaSasiedztwaS.txt")
        self.listaSasiedztwaN = self.read_file("listaSasiedztwaN.txt")
        self.tablicaS = self.read_file("tablicaS.txt")
        self.tablicaN = self.read_file("tablicaN.txt")

    @staticmethod
    def read_file(file_name: str):
        with open(os.path.join("data/", file_name), 'r') as file:
            matrix = [[int(x) for x in line.split()] for line in file]
        return matrix

    def __print_all_values(self):
        print("#####################")
        print(self.macierzIncydencji)
        print("#####################")
        print(self.macierzSasiedztwa)
        print("#####################")
        print(self.listaSasiedztwaS)
        print("#####################")
        print(self.listaSasiedztwaN)
        print("#####################")
        print(self.tablicaS)
        print("#####################")
        print(self.tablicaN)
        print("#####################")
