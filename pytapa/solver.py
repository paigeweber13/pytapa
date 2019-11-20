import puzzle

b = puzzle.Board()

def solve(puzzle):
    print(puzzle)
    solved = False
    while not solved:
        for row in range(len(puzzle)):
            for col in range(len(puzzle[row])):
                if puzzle[row][col] >= 3:
                    if puzzle[row][col] == 8:
                        if 0 < row < len(puzzle)-1 and 0 < col < len(puzzle)-1:
                            puzzle[row-1][col-1] = 1
                            puzzle[row-1][col] = 1
                            puzzle[row-1][col+1] = 1
                            puzzle[row][col-1] = 1
                            puzzle[row][col+1] = 1
                            puzzle[row+1][col-1] =1
                            puzzle[row+1][col] = 1
                            puzzle[row+1][col+1] = 1
        print(puzzle)
        break

default = [[0,0,0],[0,8,0],[0,0,0]]
solve(default)