class Board():
    puzzleSolved = [[1, 1, 1], [1, 3, 1], [1, 1, 1]]
    puzzleDefault = [[0, 0, 0], [0, 3, 0], [0, 0, 0]]
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

