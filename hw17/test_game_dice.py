import unittest
from game_dice import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.dice = Game()

    def test_throw_0_0_1_exception(self):
        with self.assertRaises(ValueError):
            self.dice.throw(0, 1, 1)

    def test_throw_0_2_2_exception(self):
        with self.assertRaises(ValueError):
            self.dice.throw(0, 2, 2)

    def test_throw_0_2_1_exception(self):
        with self.assertRaises(ValueError):
            self.dice.throw(0, 2, 1)

    def test_throw_1_2_1(self):
        result = self.dice.throw(1, 2, 1)
        self.assertEqual(result, 10)

    def test_throw_1_1_1(self):
        result = self.dice.throw(1, 1, 1)
        self.assertEqual(result, 100)

    def test_throw_2_2_2(self):
        result = self.dice.throw(2, 2, 2)
        self.assertEqual(result, 200)

    def test_throw_1_2_2(self):
        result = self.dice.throw(1, 2, 2)
        self.assertEqual(result, 20)
