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

def check_if_hint_is_satisfied(i, j, solution):
    """
    i and j are the row and column index, respectively, of the hint we're
    checking
    """
    n = len(solution)
    adjacent_blobs = []
    in_blob = False
    current_blob_size = 0
    # this order was chosen so that we move clockwise around the hint cell,
    # starting at the top-left corner
    adjustments = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

    # find all blobs
    for i_adjust, j_adjust in adjustments:
        newi = i+i_adjust
        newj = j+j_adjust
        if newi > -1 and newi < n and newj > -1 and newj < n:
            if solution[newi][newj] == 1:
                current_blob_size += 1

            if solution[newi][newj] == 0:
                if current_blob_size != 0:
                    adjacent_blobs.append(current_blob_size)
                current_blob_size = 0
    
    # check if we need to add first and last "blobs" together
    # this only matters if the adjacent cells form a circle, so we only check
    # for those that are fully within the boundaries of the puzzle
    first_square_filled = False
    last_square_filled = False

    if i-1 > -1 and j-1 > -1:
        if solution[i-1][j-1] == 1:
            first_square_filled = True

    if i+1 < n and j+1 < n:
        if solution[i][j-1] == 1:
            last_square_filled = True

    if first_square_filled and last_square_filled and len(adjacent_blobs) > 1:
        # pop returns the last thing and removes it
        # we then add that thing to the first thing
        adjacent_blobs[0] += adjacent_blobs.pop()

    adjacent_blobs.sort(reverse=True)
    blob_string = ''
    for blob in adjacent_blobs:
        blob_string += str(blob)
    
    if blob_string != '' and int(blob_string) == solution[i][j]:
        return True
    else:
        print('hint', solution[i][j], 'at', i, j, 'is not satisfied')
        print('adjacent blobs:', adjacent_blobs)
        print('blob_string:', blob_string)
        return False

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

    # does it form one continuous line?
    start_element = next(iter(filled_cell_locations))
    unexplored = explore(start_element, filled_cell_locations)
    if len(unexplored) > 0:
        print('not all filled squares are connected!')
        return False

    # TODO: are all hints satisfied?
    for (i, j) in hint_locations:
        if not check_if_hint_is_satisfied(i, j, solution):
            return False
    
    print('solution valid!')
    return True

def solve(puzzle):
    pass
