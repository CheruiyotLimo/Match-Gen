<<<<<<< HEAD
=======
# TEAMS =["Arsenal", "Man Utd", "Man City", "Tottenham Hotspurs", "Chelsea", "Liverpool"]
>>>>>>> e2d2a83c227d1f20e0b5b505e2d31b84cd86bd7c
class Match():
    TEAMS = ["Arsenal", "Man Utd", "Man City", "Tottenham Hotspurs", "Chelsea", "Liverpool"]

    def __init__(self):
        self.all_fixtures = []
<<<<<<< HEAD

=======
        
>>>>>>> e2d2a83c227d1f20e0b5b505e2d31b84cd86bd7c
    def create_all_fixtures(self, teams):
        self.all_fixtures = [(team1, team2) for team1 in teams for team2 in teams if team1 != team2]
        return self.all_fixtures

    '''This is to generate a fixture list of one individual team.'''

    def individual_team_fixtures(self, team):
        if team in self.TEAMS:
            team_fixt = [fixt for fixt in self.all_fixtures if team in fixt]
            return team_fixt
<<<<<<< HEAD
=======
# mt = Match()
# print(mt.create_all_fixtures(TEAMS))
# print(len(mt.create_all_fixtures(TEAMS)))
    
    
>>>>>>> e2d2a83c227d1f20e0b5b505e2d31b84cd86bd7c
