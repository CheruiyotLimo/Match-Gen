
class Matchday():
    TEAMS = ["Arsenal", "Man Utd", "Man City", "Tottenham Hotspurs", "Chelsea", "Liverpool"]

    def number_of_matchdays(self):
        return (len(self.TEAMS) - 1) * 2

    def number_of_fixtures_on_one_matchday(self):
        return len(self.TEAMS)/2

    def kick_off_times(self):
        valid = {
            "Saturday": [1430, 1700, 1930],
            "Sunday": [1600, 1830, 2130]
        }