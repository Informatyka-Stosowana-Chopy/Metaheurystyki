from copy import deepcopy
from abc import ABC, abstractmethod


class Algorithm(ABC):

    def __init__(self, board_start: list, board_end: list, node: int, max_depth):
        self.current_board = board_start
        self.current_board_tuple = tuple(tuple(x) for x in self.current_board)
        self.children = []
        self.valid_moves = []
        self.MOVES = 'LRUD'
        self.SOLVED_BOARD = board_end
        self.move_counter = 0
        self.solution_moves = ''
        self.node = node
        self.max_depth = max_depth
        self.current_depth = 0

    @abstractmethod
    def simulation(self):
        pass

    def _is_valid_move(self):
        """
        used in get_children

        if 0 occurred on one of the side, then the corresponding direction is removed from list valid_moves
        :return:
        """
        self.valid_moves = ['L', 'R', 'U', 'D']

        for i in range(4):
            if self.current_board[i][0] == 0:
                self.valid_moves.remove('L')
            if self.current_board[i][3] == 0:
                self.valid_moves.remove('R')
            if self.current_board[0][i] == 0:
                self.valid_moves.remove('U')
            if self.current_board[3][i] == 0:
                self.valid_moves.remove('D')

    def __search_zero(self):
        for y in range(4):
            for x in range(4):
                if self.current_board_tuple[y][x] == 0:
                    return y, x

    def get_children(self):
        """
        inside if statement append self.children with children of current board
        :return:
        """
        self._is_valid_move()
        self.children = []
        y, x = self.__search_zero()

        if 'L' in self.valid_moves:
            left_board = deepcopy(self.current_board)
            left_board[y][x], left_board[y][x - 1] = left_board[y][x - 1], left_board[y][x]
            self.children.append(self.change_list_to_tuple(left_board))
        if 'R' in self.valid_moves:
            right_board = deepcopy(self.current_board)
            right_board[y][x], right_board[y][x + 1] = right_board[y][x + 1], right_board[y][x]
            self.children.append(self.change_list_to_tuple(right_board))
        if 'U' in self.valid_moves:
            """
            to go up we have to decrease value because it isn't cartesian system.
            it starts from top left corner and this is (0, 0) point.
            """
            up_board = deepcopy(self.current_board)
            up_board[y][x], up_board[y - 1][x] = up_board[y - 1][x], up_board[y][x]
            self.children.append(self.change_list_to_tuple(up_board))
        if 'D' in self.valid_moves:
            """
            according to above, there is + to go down.
            """
            down_board = deepcopy(self.current_board)
            down_board[y][x], down_board[y + 1][x] = down_board[y + 1][x], down_board[y][x]
            self.children.append(self.change_list_to_tuple(down_board))

    def print_all_values(self):
        print(f"TURN: {self.move_counter}")
        print(self.current_board)
        print(self.SOLVED_BOARD)
        print("\n")
        print("CURRENT BOARD:")
        for line in self.current_board:
            print(line)
        print("\n")
        print("CHILDREN:")
        for child in self.children:
            print(child)
        print("\n")
        print(f"Valid moves =  {self.valid_moves}")

    @staticmethod
    def change_list_to_tuple(board: list):
        return tuple(tuple(x) for x in board)

    def update_list(self):
        self.current_board = list(list(x) for x in self.current_board_tuple)
