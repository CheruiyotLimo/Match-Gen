
from MatchGenerator.matchday import Matchday
import unittest

class TestMatchday(unittest.TestCase):
    def test_generates_number_of_matchdays(self):
        md = Matchday()
        self.assertEqual(
            md.number_of_matchdays(),
            10
        )

    def test_generates_number_of_fixtures_on_one_matchday(self):
        md = Matchday()
        self.assertEqual(
            md.number_of_fixtures_on_one_matchday(),
            3
        )