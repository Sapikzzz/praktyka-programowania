class TennisGame2:
    # Extract Variables
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        # Hardcoded player names, changed use of functions
        if player_name == self.player1_name:
            self.p1points += 1
        elif player_name == self.player2_name:
            self.p2points += 1

    def score(self):
        if self.is_tie_with_low_scores():
            return f"{self.SCORE_NAMES[self.p1points]}-All"
        if self.is_deuce():
            return "Deuce"
        if self.has_advantage():
            return f"Advantage {self.leading_player()}"
        if self.has_winner():
            return f"Win for {self.leading_player()}"
        return self.normal_score()

    # Added function for handling if statements
    def is_tie_with_low_scores(self):
        return self.p1points == self.p2points and self.p1points < 3
    
    def is_deuce(self):
        return self.p1points == self.p2points and self.p1points >= 3
    
    def has_advantage(self):
        return (
            self.p1points >= 4 or self.p2points >= 4
        ) and abs(self.p1points - self.p2points) == 1

    def has_winner(self):
        return (
            self.p1points >= 4 or self.p2points >= 4
        ) and abs(self.p1points - self.p2points) >= 2

    def leading_player(self):
        return self.player1_name if self.p1points > self.p2points else self.player2_name

    def normal_score(self):
        return f"{self.SCORE_NAMES[self.p1points]}-{self.SCORE_NAMES[self.p2points]}"
    
    # def set_p1_score(self, number):
    #     for i in range(number):
    #         self.p1_score()

    # def set_p2_score(self, number):
    #     for i in range(number):
    #         self.p2_score()

    # def p1_score(self):
    #     self.p1points += 1

    # def p2_score(self):
    #     self.p2points += 1
