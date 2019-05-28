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

        self.bid5 = Bid(3, Player(1, "Alex", 1))
        self.bid6 = Bid(3, Player(2, "Louie", 1))
        self.bid7 = Bid(3, Player(3, "BC", 2))
        self.bid8 = Bid(5, Player(4, "Leslie", 2))
        self.invalid_deal = Deal(111, self.bid5, self.bid6, self.bid7, self.bid8)


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


class TestProperties(TestDeal):
    def test_is_deal_valid(self):
        self.assertTrue(self.deal.is_deal_valid())

    def test_invalid_deal(self):
        self.assertFalse(self.invalid_deal.is_deal_valid())

    def test_total_ordered(self):
        self.assertEqual(self.deal.total_ordered, 9)

    def test_total_taken(self):
        self.deal.bid1.update_taken(4)
        self.assertEqual(self.deal.total_taken, 4)

    def test_bid_1_instance_assertion(self):
        with self.assertRaises(AssertionError):
            Deal(1, "not a bid", self.bid2, self.bid3, self.bid4)

    def test_bid_2_instance_assertion(self):
        with self.assertRaises(AssertionError):
            Deal(1, self.bid1, "not a bid", self.bid3, self.bid4)

    def test_bid_3_instance_assertion(self):
        with self.assertRaises(AssertionError):
            Deal(1, self.bid1, self.bid2, "not a bid", self.bid4)

    def test_bid_4_instance_assertion(self):
        with self.assertRaises(AssertionError):
            Deal(1, self.bid1, self.bid2, self.bid3, "not a bid")
