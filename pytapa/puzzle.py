class Board():
    puzzleSolved = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1111, 1, 1], [1, 0, 1, 7, 1], [1, 1, 1, 1, 1]]
    puzzleDefault = []
    for i in range(len(puzzleSolved)):
        puzzleDefault.append([])
        for j in range(len(puzzleSolved[i])):
            if puzzleSolved[i][j] >= 3:
                puzzleDefault[i].append(puzzleSolved[i][j])
            else:
                puzzleDefault[i].append(0)
    
    puzzle = puzzleDefault
    rectangles = []
    done = False
    solved = False

    def checkSolved(self):
        if self.puzzle == self.puzzleSolved:
            self.solved = True



class Hint():
    pass


class Cell():
    pass

