import unittest, lib.utilities as utils

class TestUtilities(unittest.TestCase):
    def test_weighted_choice_negative(self):
        with self.assertRaises(ValueError) : utils.weighted_choice([23, "dddd", 4.5], [25, -25, 50], 100)
        with self.assertRaises(ValueError) : utils.weighted_choice([23, "dddd", 4.5], [-25, -25, -50], 100)
        with self.assertRaises(ValueError) : utils.weighted_choice([23, "dddd", 4.5], [75, -25, 50], 100)

    def test_weighted_choice_not_enough_addup(self):
        with self.assertRaises(ValueError) : utils.weighted_choice([23, "dddd", 4.5], [25, 10, 50], 100)

    def test_weighted_choice_too_much_addup(self):
        with self.assertRaises(ValueError) : utils.weighted_choice([23, "dddd", 4.5], [25, 100, 50], 100)

    def test_weighted_choice_ok(self):
        test_bool = True

        for i in range(100):
            result = utils.weighted_choice([23, 300, 45], [25, 25, 50], 100)
            if not(result == 23 or result == 300 or result == 45):
                test_bool = False
        self.assertTrue(test_bool)
    
    def test_weighted_choice_ok_with_zero(self):
        test_bool = True

        for i in range(100):
            result = utils.weighted_choice([23, 300, 45], [50, 0, 50], 100)
            if result == 300:
                test_bool = False
        self.assertTrue(test_bool)

    def test_sort_different_priority(self):
        test_list = [
            ("lorem", 2),
            ("lorem", 17),
            ("lorem", 99),
            ("lorem", 46),
            ("lorem", 3),
            ("lorem", 1),
            ("lorem", 5),
            ("lorem", 20),
        ]

        sorted_list = [
            ("lorem", 1),
            ("lorem", 2),
            ("lorem", 3),
            ("lorem", 5),
            ("lorem", 17),
            ("lorem", 20),
            ("lorem", 46),
            ("lorem", 99),
        ]

        self.assertListEqual(sorted_list, utils.sort_with_priority(test_list))

    def test_sort_same_priority(self):
        test_list = [
            ("lorem", 2),
            ("aorem", 10_000),
            ("lorem", 10_000),
            ("lorem", 46),
            ("lorem", 3),
            ("lorem", 5),
            ("Gorem", 5),
            ("gorem", 5),
        ]

        sorted_list = [
            ("lorem", 2),
            ("lorem", 3),
            ("Gorem", 5),
            ("gorem", 5),
            ("lorem", 5),
            ("lorem", 46),
            ("aorem", 10_000),
            ("lorem", 10_000),
        ]
        self.assertListEqual(sorted_list, utils.sort_with_priority(test_list))