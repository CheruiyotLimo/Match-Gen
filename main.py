from MatchGenerator.match_generator import Match
from MatchGenerator.matchday import Matchday
from MatchGenerator.team import Team

mt = Match()
# teams = ["Arsenal", "Liverpool"]
all_fixtures = mt.create_all_fixtures(teams = mt.TEAMS)
print(all_fixtures)
print(len(all_fixtures))
individual_fixtures = mt.individual_team_fixtures(team = "Liverpool")
print(individual_fixtures)
print(len(individual_fixtures))
md = mt.individual_matchday_fixtures()
