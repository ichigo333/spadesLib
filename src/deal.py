class Player:
    def __init__(self, id, name, team):
        self.id = id
        self.name = name
        self.team = team

    def __init__(self, json):
        self.id = int(json['id'])
        self.name = json['name']
        self.team = int(json['team'])

    def __str__(self):
        return "Id : {id} - Name : {name} - Team : {team}".format(id=self.id, name=self.name, team=self.team)


class Team:
    def __init__(self, player1, player2):
        assert isinstance(player1, Player)
        self.player1 = player1


class Game:
    def __init__(self, team1, team2):
        pass


class Bid:
    def __init__(self, bid, player):
        self.bid = bid
        self.taken = 0
        self.player = player

    def update_taken(self, taken):
        self.taken = taken

    def update_bid(self, bid):
        pass


class Deal:
    def __init__(self, deal_number, bid1, bid2, bid3, bid4):
        self.dealNumber = deal_number
