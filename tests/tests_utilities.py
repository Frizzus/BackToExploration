import unittest, lib.utilities as utils

class TestUtilities(unittest.TestCase):
    def weighted_choice_negative(self):
        with self.assertRaises(ValueError) : utils.weighted_choice([23, "dddd", 4.5], [25, -25, 50], 100)
        with self.assertRaises(ValueError) : utils.weighted_choice([23, "dddd", 4.5], [-25, -25, -50], 100)
        with self.assertRaises(ValueError) : utils.weighted_choice([23, "dddd", 4.5], [75, -25, 50], 100)

    