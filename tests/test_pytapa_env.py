from copy import deepcopy
import unittest

from . import context
from . import sample_puzzles 

from pytapa_env.puzzle import Puzzle
import pytapa_env.solver as solver

class TestPytapaEnv(unittest.TestCase):
    def setUp(self):
        self.valid_solutions = deepcopy(sample_puzzles.valid_sample_puzzles)
        self.invalid_solutions = deepcopy(
            sample_puzzles.invalid_sample_puzzles)

    def tearDown(self):
        print('checking if sample_puzzles were edited')
        self.assertEqual(self.valid_solutions, 
            sample_puzzles.valid_sample_puzzles)
        self.assertEqual(self.invalid_solutions, 
            sample_puzzles.invalid_sample_puzzles)


    def test_constructor(self):
        for puzzle in self.valid_solutions:
            p = Puzzle(puzzle['solution'])
            self.assertEqual(p.current_state, puzzle['start'])
            self.assertEqual(p.solution, puzzle['solution'])

    def test_find_all(self):
        l = [0, 1, 3, 5, 1, 1, 5, 3, 5, 1, 1, 1]
        subs = [[1,1], [0,1], [3,5], [3]]
        expecteds = [[4, 9, 10], [0], [2, 7], [2, 7]]

        for i in range(len(subs)):
            actual = solver.find_all(l, subs[i])
            expected = expecteds[i]
            self.assertEqual(actual, expected)


    def test_validation_of_valid_tests(self):
        for puzzle in self.valid_solutions:
            assert solver.validate_solution(puzzle['solution'])

    def test_validation_of_invalid_tests(self):
        for puzzle in self.invalid_solutions:
            assert not solver.validate_solution(puzzle['solution'])
