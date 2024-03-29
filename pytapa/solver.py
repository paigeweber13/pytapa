import puzzle

b = puzzle.Board()

def solveHint(coordinate, hint, x, y):
    if coordinate[x][y] == hint:
        vr = -2
        for i in range(3):
            vr += 1
            hz = -2
            for j in range(3):
                hz += 1
                if coordinate[x+vr][y+hz] >= 2:
                    continue
                else:
                    coordinate[x+vr][y+hz] = 1

def checkHint(coordinate, hint, x, y):
    if coordinate[x][y] == hint:
        ls = []
        vr = -2
        for i in range(3):
            vr += 1
            hz = -2
            for j in range(3):
                hz += 1
                if coordinate[x+vr][y+hz] >= 2:
                    continue
                else:
                    ls.append(coordinate[x+vr][y+hz])
        ls = len(ls)
        return ls

def checkHintTop(coordinate, hint, x, y):
    if coordinate[x][y] == hint:
        ls = []
        vr = -1
        for i in range(2):
            vr += 1
            hz = -2
            for j in range(3):
                hz += 1
                if coordinate[x+vr][y+hz] >= 2:
                    continue
                else:
                    ls.append(coordinate[x+vr][y+hz])
        ls = len(ls)
        return ls

def checkHintBottom(coordinate, hint, x, y):
    if coordinate[x][y] == hint:
        ls = []
        vr = -2
        for i in range(2):
            vr += 1
            hz = -2
            for j in range(3):
                hz += 1
                if coordinate[x+vr][y+hz] >= 2:
                    continue
                else:
                    ls.append(coordinate[x+vr][y+hz])
        ls = len(ls)
        return ls

def checkHintSideL(coordinate, hint, x, y):
    if coordinate[x][y] == hint:
        ls = []
        vr = -2
        for i in range(3):
            vr += 1
            hz = -1
            for j in range(2):
                hz += 1
                if coordinate[x+vr][y+hz] >= 2:
                    continue
                else:
                    ls.append(coordinate[x+vr][y+hz])
        ls = len(ls)
        return ls

def checkHintSideR(coordinate, hint, x, y):
    if coordinate[x][y] == hint:
        ls = []
        vr = -2
        for i in range(3):
            vr += 1
            hz = -2
            for j in range(2):
                hz += 1
                if coordinate[x+vr][y+hz] >= 2:
                    continue
                else:
                    ls.append(coordinate[x+vr][y+hz])
        ls = len(ls)
        return ls          

def checkPosition(coordinate, x, y):
    if x == 0:
        position = 'top'
    elif y == 0:
        position = 'sideL'
    elif x+1 == len(coordinate):
        position = 'bottom'
    elif y+1 == len(coordinate):
        position = 'sideR'
    else:
        position = 'center'
    return position

def solveHintTop(coordinate, hint, x, y):
    if coordinate[x][y] == hint:
        vr = -1
        for i in range(2):
            vr += 1
            hz = -2
            for j in range(3):
                hz += 1
                if coordinate[x+vr][y+hz] >= 2:
                    continue
                else:
                    coordinate[x+vr][y+hz] = 1

def solveHintBottom(coordinate, hint, x, y):
    if coordinate[x][y] == hint:
        vr = -2
        for i in range(2):
            vr += 1
            hz = -2
            for j in range(3):
                hz += 1
                if coordinate[x+vr][y+hz] >= 2:
                    continue
                else:
                    coordinate[x+vr][y+hz] = 1

def solveHintSideL(coordinate, hint, x, y):
    if coordinate[x][y] == hint:
        vr = -2
        for i in range(3):
            vr += 1
            hz = -1
            for j in range(2):
                hz += 1
                if coordinate[x+vr][y+hz] >= 2:
                    continue
                else:
                    coordinate[x+vr][y+hz] = 1

def solveHintSideR(coordinate, hint, x, y):
    if coordinate[x][y] == hint:
        vr = -2
        for i in range(3):
            vr += 1
            hz = -2
            for j in range(2):
                hz += 1
                if coordinate[x+vr][y+hz] >= 2:
                    continue
                else:
                    coordinate[x+vr][y+hz] = 1

def solve(default):
    print(default)
    solved = False
    while not solved:
        for row in range(len(default)):
            for col in range(len(default[row])):
                if default[row][col] >= 3:
                    # Solves hint8 
                    if default[row][col] == 8:
                        solveHint(default, 8, row, col)
                    # Solves hint7  
                    if default[row][col] == 7:
                        ls7 = checkHint(default, 7, row, col)
                        if ls7 == 7:
                            solveHint(default, 7, row, col)
                    # Solves hint6
                    if default[row][col] == 6:
                        ls6 = checkHint(default, 6, row, col)
                        if ls6 == 6:
                            solveHint(default, 6, row, col)
                    # Solves hint5
                    if default[row][col] == 5: 
                        pos = checkPosition(default, row, col)
                        if pos == 'top':
                            solveHintTop(default, 5, row, col)
                        elif pos == 'bottom':
                            solveHintBottom(default, 5, row, col)
                        elif pos == 'sideL':
                            solveHintSideL(default, 5, row, col)
                        elif pos == 'sideR':
                            solveHintSideR(default, 5, row, col)
                        elif pos == 'center':
                            ls5 = checkHint(default, 5, row, col)
                            if ls5 == 5:
                                solveHint(default, 5, row, col)
                    # Solves hint4
                    if default[row][col] == 4:
                        pos = checkPosition(default, row, col)
                        if pos == 'top':
                            ls4 = checkHintTop(default, 4, row, col)
                            if ls4 == 4:
                                solveHintTop(default, 4, row, col)
                            else:
                                num = -1
                                for i in range(3):
                                    default[row+1][col+num] = 1
                                    num += 1
                        elif pos == 'bottom':
                            ls4 = checkHintBottom(default, 4, row, col)
                            if ls4 == 4:
                                solveHintBottom(default, 4, row, col)
                            else:
                                num = -1
                                for i in range(3):
                                    default[row-1][col+num] = 1
                                    num += 1
                        elif pos == 'sideL':
                            ls4 = checkHintSideL(default, 4, row, col)
                            if ls4 == 4:
                                solveHintSideL(default, 4, row, col)
                            else:
                                num = -1
                                for i in range(3):
                                    default[row+num][col+1] = 1
                                    num += 1
                        elif pos == 'sideR':
                            ls4 = checkHintSideR(default, 4, row, col)
                            if ls4 == 4:
                                solveHintSideR(default, 4, row, col)
                            else:
                                num = -1
                                for i in range(3):
                                    default[row+num][col-1] = 1
                                    num += 1
                        elif pos == 'center':
                            ls4 = checkHint(default, 4, row, col)
                            if ls4 == 4:
                                solveHint(default, 4, row, col)
                    # Solves hint3
                    if default[row][col] == 3:
                        pos = checkPosition(default, row, col)
                        if pos == 'top':
                            ls3 = checkHintTop(default, 3, row, col)
                            if ls3 == 3:
                                solveHintTop(default, 3, row, col)
                            else:
                                default[row+1][col] = 1
                        elif pos == 'bottom':
                            ls3 = checkHintBottom(default, 3, row, col)
                            if ls3 == 3:
                                solveHintBottom(default, 3, row, col)
                            else:
                                default[row-1][col] = 1
                        elif pos == 'sideL':
                            ls3 = checkHintSideL(default, 3, row, col)
                            if ls3 == 3:
                                solveHintSideL(default, 3, row, col)
                            else:
                                default[row][col+1] = 1
                        elif pos == 'sideR':
                            ls3 = checkHintSideR(default, 3, row, col)
                            if ls3 == 3:
                                solveHintSideR(default, 3, row, col)
                            else:
                                default[row][col-1] = 1
                        elif pos == 'center':
                            ls3 = checkHint(default, 3, row, col)
                            if ls3 == 3:
                                solveHint(default, 3, row, col)
                    # Solves hint2
                    if default[row][col] == 12:
                        pos = checkPosition(default, row, col)
                        if pos == 'top':
                            ls3 = checkHintTop(default, 12, row, col)
                            if ls3 == 2:
                                solveHintTop(default, 12, row, col)
                        elif pos == 'bottom':
                            ls3 = checkHintBottom(default, 12, row, col)
                            if ls3 == 2:
                                solveHintBottom(default, 12, row, col)
                        elif pos == 'sideL':
                            ls3 = checkHintSideL(default, 12, row, col)
                            if ls3 == 2:
                                solveHintSideL(default, 12, row, col)
                        elif pos == 'sideR':
                            ls3 = checkHintSideR(default, 12, row, col)
                            if ls3 == 2:
                                solveHintSideR(default, 12, row, col)
                        elif pos == 'center':
                            ls3 = checkHint(default, 12, row, col)
                            if ls3 == 2:
                                solveHint(default, 12, row, col)
                    # Solves hint1
                    if default[row][col] == 11:
                        pos = checkPosition(default, row, col)
                        if pos == 'top':
                            ls3 = checkHintTop(default, 11, row, col)
                            if ls3 == 1:
                                solveHintTop(default, 11, row, col)
                        elif pos == 'bottom':
                            ls3 = checkHintBottom(default, 11, row, col)
                            if ls3 == 1:
                                solveHintBottom(default, 11, row, col)
                        elif pos == 'sideL':
                            ls3 = checkHintSideL(default, 11, row, col)
                            if ls3 == 1:
                                solveHintSideL(default, 11, row, col)
                        elif pos == 'sideR':
                            ls3 = checkHintSideR(default, 11, row, col)
                            if ls3 == 1:
                                solveHintSideR(default, 11, row, col)
                        elif pos == 'center':
                            ls3 = checkHint(default, 11, row, col)
                            if ls3 == 1:
                                solveHint(default, 11, row, col)
                                                   
        print(default)
        break

puzzledefault = [[0,0,0],[0,8,0],[0,0,0]]
solution = solve(puzzledefault)
