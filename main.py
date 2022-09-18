from MatchGenerator.fixture import Fixture
from MatchGenerator.match_generator import Match
from MatchGenerator.matchday import Matchday
from MatchGenerator.team import Team

ars = Team(name = "Arsenal", stadium = "The Emirates Stadium", abbr = "ARS")
chel = Team(name = "Chelsea", stadium = "Stamford Bridge", abbr = "CHE")        
manutd = Team(name="Manchester United", stadium="Old Trafford", abbr="MUN")
mancity = Team(name="Manchester City", stadium="The Etihad Stadium", abbr="MCI")
liv = Team(name="Liverpool", stadium="Anfield", abbr="LIV")
tot = Team(name="Tottenham Hotspurs", stadium="Tottenham Hotspur Stadium", abbr="TOT")
teams = [ars, chel, mancity, manutd, liv, tot]

mt = Match()
matches = mt.create_all_fixtures(teams=teams)
fixts = []
for a, b in matches:
    fixts.append(Fixture(a, b))
print(fixts[0])
md = Matchday()
md.md_length_checker(1)
mt.individual_matchday_fixtures()