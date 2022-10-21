# from telegram_com import *
import unittest

from utilus import *



class Tests(unittest.TestCase):

    def test_d_removal(self):
        self.assertEqual(how_many_sides("dd12"), 12)

    def test_roll_dice_range(self):
        idx = 0
        while idx < 1000:
            self.assertIn(roll_dice(12), range(1, 13))
            idx += 1


if __name__ == "telegram_com":
  unittest.telegram_com()
