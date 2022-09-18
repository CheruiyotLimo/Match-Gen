from MatchGenerator.team import Team
class Fixture:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.all_fixtures = []
    
    @classmethod
    def fixture_creator(cls):
        fixture_list = []
        for team1, team2 in cls.all_fixtures:
            return fixture_list.append(Fixture(team1, team2))

    def __str__(self):
        return f"{self.team1.name} v {self.team2.name}"

    def fixture_venue(self):
        return self.team1.stadium
    
    


# ars = Team(name = "Arsenal", stadium = "The Emirates Stadium", abbr = "ARS"),
# chel = Team(name = "Chelsea", stadium = "Stamford Bridge", abbr = "CHE")
# fx = Fixture(ars, chel)
# print(fx)