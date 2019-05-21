import unittest
from src.deal import Deal
from src.bid import Bid
from src.player import Player


class TestDeal(unittest.TestCase):
    def setUp(self):
        self.bid1 = Bid(3, Player(1, "Alex", 1))
        self.bid2 = Bid(0, Player(2, "Louie", 1))
        self.bid3 = Bid(4, Player(3, "BC", 2))
        self.bid4 = Bid(2, Player(4, "Leslie", 2))
        self.deal = Deal(333, self.bid1, self.bid2, self.bid3, self.bid4)


class TestInit(TestDeal):
    def test_deal_number_is_set(self):
        self.assertEqual(self.deal.dealNumber, 333)

    def test_bid1_gets_set(self):
        self.assertEqual(self.deal.bid1, self.bid1)

    def test_bid2_gets_set(self):
        self.assertEqual(self.deal.bid2, self.bid2)

    def test_bid3_gets_set(self):
        self.assertEqual(self.deal.bid3, self.bid3)

    def test_bid4_gets_set(self):
        self.assertEqual(self.deal.bid4, self.bid4)
