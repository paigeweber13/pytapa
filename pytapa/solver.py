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
                            vr = -2
                            for i in range(len(puzzle)):
                                vr += 1
                                hz = -2
                                for j in range(len(puzzle[row])):
                                    hz += 1
                                    if puzzle[row+vr][col+hz] >= 3:
                                        continue
                                    else:
                                        puzzle[row+vr][col+hz] = 1
                                    
                                
        print(puzzle)
        break

default = [[0,0,0],[0,8,0],[0,0,0]]
solution = solve(default)
