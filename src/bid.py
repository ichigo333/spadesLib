from src.player import Player


class Bid:
    def __init__(self, ordered, player):
        self.__ordered = ordered
        self.taken = 0
        assert isinstance(player, Player)
        self.player = player

    def update_taken(self, taken):
        self.taken = taken

    @property
    def ordered(self):
        return self.__ordered

    @ordered.setter
    def ordered(self, value):
        self.__ordered = value

    def __eq__(self, other):
        return self.ordered == other.ordered and self.taken == self.taken and self.player == other.player
