import json

from src.player import Player
from src.bid import Bid
from src.deal import Deal


def import_player_from_json(json):
    return Player(int(json['id']), json['name'], int(json['team']))


if __name__ == '__main__':
    with open('players.json', 'r') as f:
        player_list = json.load(f)

    players1 = import_player_from_json(player_list['players'][0])
    players2 = import_player_from_json(player_list['players'][1])
    players3 = import_player_from_json(player_list['players'][2])
    players4 = import_player_from_json(player_list['players'][3])

    print("the end!")
