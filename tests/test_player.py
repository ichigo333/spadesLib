import unittest
from src.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player(1, "Alex", 2)
        self.player2 = Player(1, "Alex", 2)


class TestInit(TestPlayer):
    def test_id_is_set(self):
        self.assertEqual(self.player1.id, 1)

    def test_name_is_set(self):
        self.assertEqual(self.player1.name, "Alex")

    def test_team_is_set(self):
        self.assertEqual(self.player1.team, 2)


class TestMethods(TestPlayer):
    def test_to_string_format(self):
        self.assertEqual(str(self.player1), "Id : 1 - Name : Alex - Team : 2")

    def test_equal(self):
        self.assertEqual(self.player1, self.player2)
