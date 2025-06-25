'''
Game class for SushiGo.
This class represents the game board, managing players, rounds, and the winner.
'''

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sushigo.player import Player
    from sushigo.deck import Deck


class Game:
    '''
    Represents the game board.
    '''

    def __init__(self, players: list['Player'], deck: 'Deck'):
        self.players = players
        self.deck = deck
        self.rounds = 3
        self.current_round = 0
        self.winner = None

    def get_scores(self) -> dict['Player', int]:
        """
        Returns a dictionary of player names and their scores.
        """
        return {player: player.get_score(self) for player in self.players}

    # def deal_cards(self):
