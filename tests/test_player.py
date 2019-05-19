import unittest
from src.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(1, "Alex", 2)


class TestInit(TestPlayer):
    def test_id_is_set(self):
        self.assertEqual(self.player.id, 1)

    def test_name_is_set(self):
        self.assertEqual(self.player.name, "Alex")

    def test_team_is_set(self):
        self.assertEqual(self.player.team, 2)


class TestMethods(TestPlayer):
    def test_to_string_format(self):
        self.assertEqual(str(self.player), "Id : 1 - Name : Alex - Team : 2")
