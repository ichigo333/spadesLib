class Player:
    def __init__(self, id, name, team):
        self.id = id
        self.name = name
        self.team = team
    #
    # def __init__(self, json):
    #     self.id = int(json['id'])
    #     self.name = json['name']
    #     self.team = int(json['team'])

    def __str__(self):
        return "Id : {id} - Name : {name} - Team : {team}".format(id=self.id, name=self.name, team=self.team)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.team == other.team
