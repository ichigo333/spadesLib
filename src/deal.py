from src.player import Player


class Team:
    def __init__(self, player1, player2):
        assert isinstance(player1, Player)
        self.player1 = player1


class Game:
    def __init__(self, team1, team2):
        pass


class Deal:
    def __init__(self, deal_number, bid1, bid2, bid3, bid4):
        self.dealNumber = deal_number
