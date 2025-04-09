class TennisGame1:
    # 1. Extract Variable
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        # changed hardcoded player names
        if player_name == self.player1_name:
            self.p1points += 1
        elif player_name == self.player2_name:
            self.p2points += 1

    # Added functions for returning score
    def endgame_score(self):
        score_diff = self.p1points - self.p2points
        if score_diff == 1:
            return "Advantage player1"
        elif score_diff == -1:
            return "Advantage player2"
        elif score_diff >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
        
    def even_score(self):
        if self.p1points < 3:
            return f"{self.SCORE_NAMES[self.p1points]}-All"
        return "Deuce"

    def score(self):
        result = ""
        # Deleted temp_score - not used after refactor
        if self.p1points == self.p2points:
            result = self.even_score()
        elif self.p1points >= 4 or self.p2points >= 4:
            result = self.endgame_score()
        else:
            # Instead of for loop, just return current score with the use of SCORE_NAMES
            return f"{self.SCORE_NAMES[self.p1points]}-{self.SCORE_NAMES[self.p2points]}"
        return result
