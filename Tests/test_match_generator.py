from MatchGen.MatchGenerator.match_generator import Match
import unittest

class TestMatchGenerator(unittest.TestCase):
    def test_creates_list_of_all_matches(self):
        teams = ["Arsenal", "Liverpool"]
        mt = Match()

        all = mt.create_all_fixtures(teams = teams)
        self.assertEqual(
            all,
            [("Arsenal", "Liverpool"), 
            ("Liverpool", "Arsenal")]
        )

    def test_generates_individual_team_fixtures(self):
        teams = ["Arsenal", "Liverpool", "Chelsea"]
        m = Match()
        m.create_all_fixtures(teams = teams)

        self.assertEqual(
                m.individual_team_fixtures(team = "Liverpool"),
            [
                ("Arsenal", "Liverpool"),
                ("Liverpool", "Arsenal"),
                ("Liverpool", "Chelsea"),
                ("Chelsea", "Liverpool")
            ])

    def test_creates_matchday_fixtures(self):
        teams = ["Arsenal", "Liverpool", "Chelsea", "Man Utd"]
        m = Match()
        m.create_all_fixtures(teams = teams)

        self.assertEqual(
            m.individual_matchday_fixtures(),
            [
                ("Arsenal", "Liverpool"),
                ("Chelsea", "Man Utd")
            ]
        )
    