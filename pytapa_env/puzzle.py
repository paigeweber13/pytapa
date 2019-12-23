from copy import deepcopy

EMPTY_CELL = -1
FILLED_CELL = -2

cell_codes = set([
    FILLED_CELL, EMPTY_CELL,

    # all other codes are hints. 
    # these hints are pretty intuitive, you just have one or more in a cell
    8, 7, 6, 5, 51, 4, 41, 42, 3, 33, 32, 311, 31, 22, 2, 21, 221, 211,
    1, 11, 111, 1111, 0
])

class Puzzle():
    def __init__(self, solution):
        # TODO: validate solution here:
        self.solution = solution
        self.current_state = deepcopy(solution)

        # for current state, nothing is filled in initially
        for row_i in range(len(self.current_state)):
            for col_i in range(len(self.current_state[row_i])):
                if self.current_state[row_i][col_i] == FILLED_CELL:
                    self.current_state[row_i][col_i] = EMPTY_CELL 

