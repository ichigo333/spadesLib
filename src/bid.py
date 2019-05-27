class Bid:
    def __init__(self, ordered, player):
        self.ordered = ordered
        self.taken = 0
        self.player = player

    def update_taken(self, taken):
        self.taken = taken

    #convert to properties?
    def update_ordered(self, ordered):
        self.ordered = ordered

    def __eq__(self, other):
        return self.ordered == other.ordered and self.taken == self.taken and self.player == other.player
