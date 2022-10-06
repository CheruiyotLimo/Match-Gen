
class Team():
    def __init__(self, name, stadium, abbr):
        self.name = name
        self.stadium = stadium
        self.abbr = abbr
        self.fixtures = []
    

    def __str__(self):
        return self.name
# TEAMS = [ars, chel, mancity, manutd, liv, tot]
    # def team_fixtures(self):
    #     return self.all_fixtures.individual_team_fixtures(self.name)