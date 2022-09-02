
class Team():
    def __init__(self, name, stadium, abbr):
        self.name = name
        self.stadium = stadium
        self.abbr = abbr
        self.fixtures = []
    
ars = Team(name = "Arsenal", stadium = "The Emirates Stadium", abbr = "ARS"),
chel = Team(name = "Chelsea", stadium = "Stamford Bridge", abbr = "CHE")        
manutd = Team(name="Manchester United", stadium="Old Trafford", abbr="MUN")
mancity = Team(name="Manchester City", stadium="The Etihad Stadium", abbr="MCI")
liv = Team(name="Liverpool", stadium="Anfield", abbr="LIV")
tot = Team(name="Tottenham Hotspurs", stadium="Tottenham Hotspur Stadium", abbr="TOT")

TEAMS = [ars, chel, mancity, manutd, liv, tot]
    # def team_fixtures(self):
    #     return self.all_fixtures.individual_team_fixtures(self.name)