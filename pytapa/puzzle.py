class Board():
    puzzleSolved = [[1, 1, 1, 1, 1], [1, 2, 1, 2, 1], [1, 1, 1111, 1, 1], [1, 2, 1, 7, 1], [1, 1, 1, 1, 1]]
    puzzleDefault = []
    
    def createDefault(self):
        for i in range(len(self.puzzleSolved)):
            self.puzzleDefault.append([])
            for j in range(len(self.puzzleSolved[i])):
                if self.puzzleSolved[i][j] >= 3:
                    self.puzzleDefault[i].append(self.puzzleSolved[i][j])
                else:
                    self.puzzleDefault[i].append(0)
    
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

