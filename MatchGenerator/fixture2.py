from MatchGenerator import team
class Fixture2(team.Team):
    def __init__(self, fixt):
        self.fixt = fixt
        self.class_fixtures = []
    
    def fixture_class_gen(self):
        for md in self.gen_fixtures:
            for i in self.gen_fixtures[md]:
                self.class_fixtures.append(Fixture2(i))
        return self.class_fixtures