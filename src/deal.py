from src.bid import Bid


class Deal:
    def __init__(self, deal_number, bid1, bid2, bid3, bid4):
        self.dealNumber = deal_number
        assert isinstance(bid1, Bid)
        assert isinstance(bid2, Bid)
        assert isinstance(bid3, Bid)
        assert isinstance(bid4, Bid)
        self.bid1 = bid1
        self.bid2 = bid2
        self.bid3 = bid3
        self.bid4 = bid4

    @property
    def total_ordered(self) -> int:
        return self.bid1.ordered + self.bid2.ordered + self.bid3.ordered + self.bid4.ordered

    @property
    def total_taken(self) -> int:
        return self.bid1.taken + self.bid2.taken + self.bid3.taken + self.bid4.taken

    def is_deal_valid(self):
        if self.total_ordered <= 13:
            return True

        return False
