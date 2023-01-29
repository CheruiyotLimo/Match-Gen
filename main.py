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
teams = [ars, chel, manutd, mancity, liv, tot]

md = Matchday()
md.create_all_fixtures(teams)
print(len(md.create_all_fixtures(teams)))
fixts = []
for a, b in md.fixtures_all:
    fixts.append(Fixture(a, b))
print(fixts[1])
print(len(fixts))

md.md_length_checker(1)
print(md.number_of_matchdays())
print(md.number_of_fixtures_on_one_matchday())
md.individual_matchday_fixtures_generator()
# md.fixture_counter()
# # print(len(fixts))
# md.md_illustrator()
# # for x in md.gen_fixtures["Matchday 1"]:
# #     print(x)
print(md.gen_fixtures["Matchday 1"][0][0].name)