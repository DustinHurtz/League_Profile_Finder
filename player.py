# Player class
# Holds the player's username, Rank, League Points, and winratio

class Player:
    # Player constructor, takes in username, League Points, and winratio
    def __init__(self, user_name, rank, lp, win_ratio):
        self.user_name = user_name
        self.rank = rank
        self.lp = lp
        self.win_ratio = win_ratio

    # Getters for the Player class
    def get_user_name(self):
        return self.user_name

    def get_rank(self):
        return self.rank

    def get_lp(self):
        return self.lp

    def get_win_ratio(self):
        return self.win_ratio