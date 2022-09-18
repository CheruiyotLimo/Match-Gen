
class Matchday():
    def __init__(self):
        self.fixtures_all = []
        
    TEAMS = ["Arsenal", "Man Utd", "Man City", "Tottenham Hotspurs", "Chelsea", "Liverpool"]

    def number_of_matchdays(self):
        total = (len(self.TEAMS) - 1) * 2
        print(total)
        return {f"Matchday {day + 1}": [1, 1] for day in range(total)}
        

    def number_of_fixtures_on_one_matchday(self):
        return len(self.TEAMS)//2

    # def kick_off_times(self):
    #     valid = {
    #         "Saturday": [1430, 1700, 1930],
    #         "Sunday": [1600, 1830, 2130]
    #     }

    def md_length_checker(self, day_int):                            ##Thinking of using this as a decorator.
        '''Decorator for checking number of matchday matches.'''
        j = f"Matchday {day_int}"
        if len(self.number_of_matchdays()[j]) > self.number_of_fixtures_on_one_matchday():
                raise ValueError("Exceeded maximum number of matches on one matchday.")
        else:
                print("Valid")
        
# mt = Matchday()
# print(mt.number_of_matchdays())
# print(mt.number_of_fixtures_on_one_matchday())
# mt.md_length_checker(2)