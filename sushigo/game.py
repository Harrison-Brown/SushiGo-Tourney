from sushigo.player import Player

class Game:
    '''
    Represents the game board.
    '''
    def __init__(self):
        self.players = []
        self.rounds = 0
        self.current_round = 0
        self.winner = None

    def add_player(self, player: Player):
        """
        Adds a player to the game.
        """
        if player not in self.players:
            self.players.append(player)
            player.game = self
        else:
            raise ValueError(f"{player.name} is already in the game.")