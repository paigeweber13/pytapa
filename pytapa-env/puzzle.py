cell_codes = set([
    # 0 means the cell is not filled 
    # 1 means the cell is filled 
    0, 1,

    # all other codes are hints. 
    # these hints are pretty intuitive, you just have one or more in a cell
    8, 7, 6, 5, 51, 4, 41, 42, 3, 33, 32, 311, 31, 22, 2, 21, 221, 211,
    # the hints that involve one have one more digit than the actual number of
    # hints. For instance, 11 is a cell with only '1' as the hint. 111 is a
    # cell with '1   1' as the hint (two ones)
    11, 111, 1111, 11111
])

class Puzzle():
    def __init__(self, solution):
        # TODO: validate solution here:
        self.solution = solution
        self.current_state = solution

        # for current state, nothing is filled in initially
        for row_i in range(len(self.current_state)):
            for col_i in range(len(self.current_state[row_i])):
                if self.current_state[row_i][col_i] == 1:
                    self.current_state[row_i][col_i] = 0

