import os


class Reader:

    @staticmethod
    def read() -> tuple:
        with open(os.path.join(os.getcwd(), "data/board_start.txt"), 'r') as file:
            board_start = [[int(x) for x in line.split()] for line in file]

        with open(os.path.join(os.getcwd(), "data/board_end.txt"), 'r') as file:
            board_end = [[int(x) for x in line.split()] for line in file]

        return board_start, board_end

    @staticmethod
    def save(content_to_save: str):
        with open(os.path.join(os.getcwd(), "results/pattern.txt"), 'w') as file:
            file.write(content_to_save)
