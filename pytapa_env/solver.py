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

def explore(start_point: (int, int), still_unexplored: set) -> set:
    """
    still_explored should contain indices of filled squares in the puzzle
    """
    i = start_point[0]
    j = start_point[1]

    # if this point is a 1
    if start_point in still_unexplored:
        # remove self to prevent infinte loops
        still_unexplored.remove(start_point)
        
        # explore up, down, left, and right
        still_unexplored = explore((i-1, j), still_unexplored)
        still_unexplored = explore((i+1, j), still_unexplored)
        still_unexplored = explore((i, j-1), still_unexplored)
        still_unexplored = explore((i, j+1), still_unexplored)

    # if point is a 0, still_unexplored will not be edited before returning it
    return still_unexplored

def validate_solution(solution):
    print('checking solution')
    print(solution)
    n = len(solution)
    filled_cell_locations = set()
    hint_locations = set()

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
                        print('there is a 2x2 block in this solution!')
                        return False
        
        for col_i in range(len(solution[row_i])):
            # is every cell a valid code?
            if solution[row_i][col_i] not in puzzle.cell_codes:
                print('Invalid entry:', solution[row_i][col_i])
                return False
            
            # store locations of 1s for checking continuous path later
            if solution[row_i][col_i] == 1:
                filled_cell_locations.add((row_i, col_i))
            # store locations of hints for checking hints later
            else:
                hint_locations.add((row_i, col_i))

    if len(filled_cell_locations) == 0:
        print('solution has no filled cells! That can\'t be right.... can it?')
        return False

    # TODO: does it form one continuous line?
    # if len(filled_cell_locations) > 0:
    start_element = next(iter(filled_cell_locations))
    unexplored = explore(start_element, filled_cell_locations)
    if len(unexplored) > 0:
        print('not all filled squares are connected!')
        return False

    # TODO: are all hints satisfied?
    
    return True

def solve(puzzle):
    pass
