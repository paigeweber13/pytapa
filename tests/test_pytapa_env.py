import unittest

from . import context
from . import sample_puzzles 

from pytapa_env.puzzle import Puzzle
import pytapa_env.solver as solver

class TestPytapaEnv(unittest.TestCase):
    def test_constructor(self):
        for puzzle in sample_puzzles.valid_sample_puzzles:
            p = Puzzle(puzzle['solution'])
            self.assertEqual(p.current_state, puzzle['start'])

    def test_find_all(self):
        l = [0, 1, 3, 5, 1, 1, 5, 3, 5, 1, 1, 1]
        subs = [[1,1], [0,1], [3,5], [3]]
        expecteds = [[4, 9, 10], [0], [2, 7], [2, 7]]

        for i in range(len(subs)):
            actual = solver.find_all(l, subs[i])
            expected = expecteds[i]
            self.assertEqual(actual, expected)


    def test_validation_of_valid_tests(self):
        for puzzle in sample_puzzles.valid_sample_puzzles:
            print('testing with puzzle', puzzle)
            assert solver.validate_solution(puzzle['solution'])

    def test_validation_of_invalid_tests(self):
        for puzzle in sample_puzzles.invalid_sample_puzzles:
            assert not solver.validate_solution(puzzle['solution'])
