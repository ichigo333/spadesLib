import json
from deal import Player
from deal import Team

if __name__ == '__main__':
    with open('players.json', 'r') as f:
        player_list = json.load(f)

    players1 = Player(player_list['players']['player'][0])
    players2 = Player(player_list['players']['player'][1])
    players3 = Player(player_list['players']['player'][2])
    players4 = Player(player_list['players']['player'][3])

    print('hello')
