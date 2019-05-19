class Bid:
    def __init__(self, bid, player):
        self.bid = bid
        self.taken = 0
        self.player = player

    def update_taken(self, taken):
        self.taken = taken

    def update_bid(self, bid):
        self.bid = bid
