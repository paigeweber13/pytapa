from . import puzzle
from . import solver

def find_all(l: list, sub: list) -> list:
    """
    returns list of indices of all finds
    """
    res = []

    for l_i in range(len(l)):
        match = True

        for sub_i in range(len(sub)):
            if l_i+sub_i >= len(l) or l[l_i+sub_i] != sub[sub_i]:
                match = False
                break

        if match:
            res.append(l_i)
    
    return res

def validate_solution(solution):
    # TODO: implement validation
    #   * does it form one continuous line?
    #   * are there no blocks of 2x2 or bigger?
    #   * does it obey hints?
    n = len(solution)
    filled_cell_locations = []

    for row_i in range(len(solution)):
        # is it square? are all rows of same length?
        if len(solution[row_i]) != n:
            print('Matrix not square! Row', row_i, ' is of length', 
                  len(solution[row_i]), ' but matrix has height', n)
            return False

        # search for 2x2 blocks
        if row_i + 1 != len(solution):
            locations_this_row = solver.find_all(solution[row_i], [1,1])
            locations_next_row = solver.find_all(solution[row_i+1], [1,1])
            for loc_this_row in locations_this_row:
                for loc_next_row in locations_next_row:
                    if loc_this_row == loc_next_row:
                        return False
        
        for col_i in range(len(solution[row_i])):
            # is every cell a valid code?
            if solution[row_i][col_i] not in puzzle.cell_codes:
                print('Invalid entry:', solution[row_i][col_i])
                return False
            
            # store locations of 1s for checking continuous path later
            if solution[row_i][col_i] == 1:
                filled_cell_locations.append((row_i, col_i))
    
    return True

def solve(puzzle):
    pass
