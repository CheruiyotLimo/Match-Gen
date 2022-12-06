import os
import sys
import unittest

path = os.path.dirname(os.path.realpath(__file__))
if path not in sys.path:
    sys.path.append(path)
sys.path.append(os.path.join(os.path.dirname(__file__), "../MatchGenerator/"))

import match_generator as match

class TestMatchGenerator(unittest.TestCase):
    def test_creates_list_of_all_matches(self):
        teams = ["Arsenal", "Liverpool"]
        mt = match.Match()

        all = mt.create_all_fixtures(teams = teams)
        self.assertEqual(
            all,
            [("Arsenal", "Liverpool"), 
            ("Liverpool", "Arsenal")]
        )

    def test_generates_individual_team_fixtures(self):
        teams = ["Arsenal", "Liverpool", "Chelsea"]
        m = match.Match()
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
        m = match.Match()
        m.create_all_fixtures(teams = teams)

        self.assertEqual(
            m.individual_matchday_fixtures(),
            [
                ("Arsenal", "Liverpool"),
                ("Chelsea", "Man Utd")
            ]
        )
    