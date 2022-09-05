
from MatchGen.MatchGenerator.team import Team
import unittest

class TestTeam(unittest.TestCase):
    def test_team_has_name_and_stadium(self):
        ars = Team(name = "Arsenal", stadium = "Emirates")

        self.assertEqual(
            ars.name,
            "Arsenal"
        )
        self.assertEqual(
            ars.stadium,
            "Emirates"
        )
    
    # def test_generates_individual_team_fixtures(self):
    #     liv = Team(name = "Liverpool", stadium = "Anfield")
    #     liv.fixtures = [("Arsenal, Liverpool"), ("Arsenal", "Chelsea"), ("Chelsea", "Liverpool")]

    #     self.assertEqual(liv.team_fixtures(),
    #     [("Arsenal, Liverpool"), ("Chelsea", "Liverpool")])
