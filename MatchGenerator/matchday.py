TEAMS = ["Arsenal", "Man Utd", "Man City", "Tottenham Hotspurs", "Chelsea", "Liverpool"]

class Matchday():
    def __init__(self):
        self.fixtures_all = []
        
    def create_all_fixtures(self, teams = TEAMS):
        self.fixtures_all = [(team1, team2) for team1 in teams for team2 in teams if team1 != team2]
        print(self.fixtures_all)
        return

    def number_of_matchdays(self):
        total = (len(TEAMS) - 1) * 2
        print(total)
        return {f"Matchday {day}": [] for day in range(1, total+1)}   

    def number_of_fixtures_on_one_matchday(self):
        return len(TEAMS)//2

    # def kick_off_times(self):
    #     valid = {
    #         "Saturday": [1430, 1700, 1930],
    #         "Sunday": [1600, 1830, 2130]
    #     }

    def individual_matchday_fixtures(self):
        '''All matches to be played on one MatchDay.''' 
        matchdays = self.number_of_matchdays()
        for md in matchdays:
            checker = []
            while len(matchdays[md]) < self.number_of_fixtures_on_one_matchday(): #Need a condition to loop it back to find fixtures 
                for fixture in self.fixtures_all:                                 #that had been passed over the first time  
                    team1, team2 = fixture
                    if team1 not in checker and team2 not in checker:
                        checker.append(team1)
                        checker.append(team2)
                        matchdays[md].append(fixture)
                        self.fixtures_all.remove(fixture)
                
            checker.clear()
        return matchdays

    def md_length_checker(self, day_int):                            ##Thinking of using this as a decorator.
        '''Decorator for checking number of matchday matches.'''
        j = f"Matchday {day_int}"
        if len(self.number_of_matchdays()[j]) > self.number_of_fixtures_on_one_matchday():
                raise ValueError("Exceeded maximum number of matches on one matchday.")
        else:
                print("Valid")
        
mt = Matchday()
mt.create_all_fixtures()
print(mt.number_of_matchdays())
print(mt.number_of_fixtures_on_one_matchday())
mt.md_length_checker(2)
print(mt.individual_matchday_fixtures())