import unittest
from src.bid import Bid
from src.player import Player


class TestBid(unittest.TestCase):
    def setUp(self):
        self.player = Player(1, "Alex", 1)
        self.bid1 = Bid(1, self.player)
        self.bid2 = Bid(1, self.player)
        self.bid3 = Bid(1, Player(2, "BC", 1))
        self.bid4 = Bid(4, self.player)


class TestInit(TestBid):
    def test_ordered_is_set(self):
        self.assertEqual(self.bid1.ordered, 1)

    def test_player_is_set(self):
        self.assertIsInstance(self.bid1.player, Player)

    def test_player_id_matches(self):
        self.assertEqual(self.bid1.player, self.player)

    def test_taken_default(self):
        self.assertEqual(self.bid1.taken, 0)


class TestMethods(TestBid):
    def test_taken_can_be_updated(self):
        self.bid1.update_taken(1)
        self.assertEqual(self.bid1.taken, 1)

    def test_ordered_can_be_updated(self):
        self.bid1.update_ordered(3)
        self.assertEqual(self.bid1.ordered, 3)

    def test_equal(self):
        self.assertEqual(self.bid1, self.bid2)

    def test_not_equal_due_to_player(self):
        self.assertNotEqual(self.bid1, self.bid3)

    def test_not_equal_due_to_bid(self):
        self.assertNotEqual(self.bid1, self.bid4)
