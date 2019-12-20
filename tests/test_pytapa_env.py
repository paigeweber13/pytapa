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

    def test_validation_of_valid_tests(self):
        for puzzle in sample_puzzles.valid_sample_puzzles:
            self.assertTrue(solver.validate_solution(puzzle['solution']))

    def test_validation_of_invalid_tests(self):
        for puzzle in sample_puzzles.invalid_sample_puzzles:
            self.assertFalse(solver.validate_solution(puzzle['solution']))
