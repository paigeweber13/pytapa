from . import puzzle

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
        
        for col_i in range(len(solution[row_i])):
            # is every cell a valid code?
            if solution[row_i][col_i] not in puzzle.cell_codes:
                print('Invalid entry:', solution[row_i][col_i])
                return False
            if solution[row_i][col_i] == 1:
                filled_cell_locations.append((row_i, col_i))
    
    return True

def solve(puzzle):
    pass
