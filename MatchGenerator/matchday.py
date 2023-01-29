TEAMS = ["Arsenal", "Man Utd", "Man City", "Tottenham Hotspurs", "Chelsea", "Liverpool"]
<<<<<<< HEAD
import random
=======
from MatchGenerator.fixture import Fixture
>>>>>>> e2d2a83c227d1f20e0b5b505e2d31b84cd86bd7c


class Matchday:
    def __init__(self):
        self.fixtures_all = []
<<<<<<< HEAD

    def create_all_fixtures(self, teams=TEAMS):
        self.fixtures_all = [(team1, team2) for team1 in teams for team2 in teams if team1 != team2]
        # print(self.fixtures_all)
        # print(len(self.fixtures_all))
        return
=======
        self.gen_fixtures = []
        
    def create_all_fixtures(self, teams):
        self.fixtures_all = [(team1, team2) for team1 in teams for team2 in teams if team1 != team2]
        # print(self.fixtures_all)
        return self.fixtures_all
>>>>>>> e2d2a83c227d1f20e0b5b505e2d31b84cd86bd7c

    # @property
    def number_of_matchdays(self):
        total = (len(TEAMS) - 1) * 2
<<<<<<< HEAD
        print(total)
        return {f"Matchday {day}": [] for day in range(1, total + 1)}
=======
        # print(total)
        self.gen_fixtures = {f"Matchday {day}": [] for day in range(1, total+1)}   
        return self.gen_fixtures
>>>>>>> e2d2a83c227d1f20e0b5b505e2d31b84cd86bd7c

    def number_of_fixtures_on_one_matchday(self):
        return len(TEAMS) // 2

    # def kick_off_times(self):
    #     valid = {
    #         "Saturday": [1430, 1700, 1930],
    #         "Sunday": [1600, 1830, 2130]
    #     }

<<<<<<< HEAD
    def individual_matchday_fixtures(self):
        '''All matches to be played on one MatchDay.'''
        matchdays = self.number_of_matchdays()
        random.shuffle(self.fixtures_all)
        for md in matchdays:
            checker = []
            while len(matchdays[md]) < self.number_of_fixtures_on_one_matchday():            # Need a condition to loop it back to find fixtures
                for fixture in self.fixtures_all:                                           # that had been passed over the first time
                    team1, team2 = fixture
                    if team1 not in checker and team2 not in checker:
                        checker.append(team1)
                        checker.append(team2)
                        matchdays[md].append(fixture)
                        self.fixtures_all.remove(fixture)
                break
            checker.clear()
        if self.fixtures_all:
            self.individual_matchday_fixtures()
        # print(len(self.fixtures_all))
        print(len(self.fixtures_all))
        return matchdays
=======
    def individual_matchday_fixtures_generator(self):
        '''All matches to be played on one MatchDay.''' 

        while len(self.fixtures_all):
            for md in self.gen_fixtures:
                checker = []
                for i in range(len(self.fixtures_all)):                                    
                    team1, team2 = self.fixtures_all[i]
                    if team1 in checker or team2 in checker:
                        continue
                    checker.append(team1)
                    checker.append(team2)
                    self.gen_fixtures[md].append(self.fixtures_all[i])        
                    self.fixtures_all.remove(self.fixtures_all[i])
                    break
        return self.gen_fixtures

    def fixture_counter(self):
        count = 0
        for fixts in self.gen_fixtures:
            print(f"{fixts}: {len(self.gen_fixtures[fixts])}")
            count += len(self.gen_fixtures[fixts])
        print(count)
    # def individual_matchdays_printer(self, day: int):
    #     return f"Fixtures on Matchday {d}"
    def md_illustrator(self):
        for i in self.gen_fixtures:
            print(i)
            for j in self.gen_fixtures[i]:
                print(j)
>>>>>>> e2d2a83c227d1f20e0b5b505e2d31b84cd86bd7c

    def md_length_checker(self, day_int):                                       #Thinking of using this as a decorator.
        '''Decorator for checking number of matchday matches.'''
        j = f"Matchday {day_int}"
        # print(j)
        # print(self.number_of_matchdays)
        if len(self.number_of_matchdays()[j]) > self.number_of_fixtures_on_one_matchday():
            raise ValueError("Exceeded maximum number of matches on one matchday.")
        else:
<<<<<<< HEAD
            print("Valid")

    def class_interpretor(self):
        pass

    


mt = Matchday()
mt.create_all_fixtures()
# print(mt.number_of_matchdays)
# print(mt.number_of_fixtures_on_one_matchday())
# mt.md_length_checker(2)
print(mt.individual_matchday_fixtures())
=======
                print("Valid")
        
# mt = Matchday()
# mt.create_all_fixtures()
# print(mt.number_of_matchdays())
# print(mt.number_of_fixtures_on_one_matchday())
# mt.md_length_checker(2)
# print(mt.individual_matchday_fixtures())
>>>>>>> e2d2a83c227d1f20e0b5b505e2d31b84cd86bd7c
