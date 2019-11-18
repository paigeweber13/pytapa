class Board():
    puzzleSolved = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    puzzleDefault = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    puzzle = puzzleDefault
    rectangles = []
    solved = False

    def checkSolved(self):
        if self.puzzle == self.puzzleSolved:
            self.solved = True


class Hint():
    pass


class Cell():
    pass

