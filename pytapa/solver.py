import puzzle

b = puzzle.Board()

def solveHint(coordinate, hint, x, y):
    if coordinate[x][y] == hint:
        vr = -2
        for i in range(len(coordinate)):
            vr += 1
            hz = -2
            for j in range(len(coordinate[x])):
                hz += 1
                if coordinate[x+vr][y+hz] >= 2:
                    continue
                else:
                    coordinate[x+vr][y+hz] = 1

def checkHint(coordinate, hint, x, y):
    if coordinate[x][y] == hint:
        ls = []
        vr = -2
        for i in range(len(coordinate)):
            vr += 1
            hz = -2
            for j in range(len(coordinate[x])):
                hz += 1
                if coordinate[x+vr][y+hz] >= 2:
                    continue
                else:
                    ls.append(coordinate[x+vr][y+hz])
        ls = len(ls)
        return ls

def solve(default):
    print(default)
    solved = False
    while not solved:
        for row in range(len(default)):
            for col in range(len(default[row])):
                if default[row][col] >= 3:
                    # Solves hint8 
                    solveHint(default, 8, row, col)
                    # Solves hint7  
                    ls = checkHint(default, 7, row, col)
                    if ls == 7:
                        solveHint(default, 7, row, col)
                                                   
        print(default)
        break

puzzledefault = [[0,2,0],[0,7,0],[0,0,0]]
solution = solve(puzzledefault)
