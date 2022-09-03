

from calendar import c


class Match():
    TEAMS =["Arsenal", "Man Utd", "Man City", "Tottenham Hotspurs", "Chelsea", "Liverpool"]
    def __init__(self):
        self.all_fixtures = []
    
    
    def create_all_fixtures(self, teams):
        self.all_fixtures = [(team1, team2) for team1 in teams for team2 in teams if team1 != team2]
        return self.all_fixtures

    '''This is to generate a fixture list of one individual team.'''
    def individual_team_fixtures(self, team):
        if team in self.TEAMS:
            team_fixt = [fixt for fixt in self.all_fixtures if team in fixt]
            return team_fixt
    
    '''All matches to be played on one Match Day.''' 
    def individual_matchday_fixtures(self):
        match_day_1 = [] #Wil iterate over dict in matchday.
        teamlist = [] #Will ammend to use value of md key.
        max_number = len(self.TEAMS)/2
        for fixture in self.all_fixtures:
            team1, team2 = fixture
            if team1 not in teamlist and team2 not in teamlist:
                teamlist.append(team1)
                teamlist.append(team2)
                match_day_1.append((team1, team2))
        return match_day_1