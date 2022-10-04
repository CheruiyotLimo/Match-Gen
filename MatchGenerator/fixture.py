from MatchGenerator.team import Team
class Fixture:
    def __init__(self, fixture):
        self.fixture = fixture
        self.all_fixtures = []
    
    @classmethod
    def fixture_creator(cls):
        fixture_list = []
        for fixture in cls.all_fixtures:
            return fixture_list.append(Fixture(fixture))

    def __str__(self):
        return f"{self.team1.name} v {self.team2.name}"

    def fixture_venue(self):
        return self.team1.stadium
    
    


ars = Team(name = "Arsenal", stadium = "The Emirates Stadium", abbr = "ARS"),
chel = Team(name = "Chelsea", stadium = "Stamford Bridge", abbr = "CHE")
fixt = (ars, chel)
fx = Fixture(fixt)
print(fx)