import unittest
from bid import Bid
from deal import Player


class TestBid(unittest.TestCase):
    def setUp(self):
        player = Player(1, "Alex", 1)
        self.bid = Bid(1, player)


class TestInit(TestBid):
    def test_bid_is_set(self):
        self.assertEqual(self.bid.bid, 1)

    def test_player_name_is_set(self):
        self.assertEqual(self.bid.player.name, "Alex")

    def test_player_team_is_set(self):
        self.assertEqual(self.bid.player.team, 1)

    def test_taken_default(self):
        self.assertEqual(self.bid.taken, 0)


class TestMethods(TestBid):
    def test_taken_can_be_updated(self):
        self.bid.update_taken(1)
        self.assertEqual(self.bid.taken, 1)