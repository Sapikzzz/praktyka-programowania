class TennisGame3:
    score_names = ["Love", "Fifteen", "Thirty", "Forty"]
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        elif player_name == self.player2_name:
            self.player2_points += 1

    def is_early_game(self):
        return ((self.player1_points < 4 and self.player2_points < 4) and (self.player1_points + self.player2_points < 6))
    
    def leading_player(self):
        return self.player1_name if self.player1_points > self.player2_points else self.player2_name
    
    def early_game_score(self):
        player1_score_text = self.score_names[self.player1_points]
        player2_score_text = self.score_names[self.player2_points]
        return f"{player1_score_text}-All" if self.player1_points == self.player2_points else f"{player1_score_text}-{player2_score_text}"

    def late_game_score(self):
        leading_player = self.leading_player()
        point_difference = abs(self.player1_points - self.player2_points)
        return f"Advantage {leading_player}" if point_difference == 1 else f"Win for {leading_player}"
    
    def score(self):
        if self.is_early_game():
            return self.early_game_score()
        else:
            if self.player1_points == self.player2_points:
                return "Deuce"
            return self.late_game_score()
