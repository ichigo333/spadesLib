import unittest
from src.bid import Bid
from src.player import Player


class TestBid(unittest.TestCase):
    def setUp(self):
        self.player = Player(1, "Alex", 1)
        self.bid = Bid(1, self.player)


class TestInit(TestBid):
    def test_bid_is_set(self):
        self.assertEqual(self.bid.bid, 1)

    def test_player_is_set(self):
        self.assertIsInstance(self.bid.player, Player)

    def test_player_id_matches(self):
        self.assertEqual(self.bid.player, self.player)

    def test_taken_default(self):
        self.assertEqual(self.bid.taken, 0)


class TestMethods(TestBid):
    def test_taken_can_be_updated(self):
        self.bid.update_taken(1)
        self.assertEqual(self.bid.taken, 1)

    def test_bid_can_be_updated(self):
        self.bid.update_bid(3)
        self.assertEqual(self.bid.bid, 3)
