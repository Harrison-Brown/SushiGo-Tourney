'''
Player class for the Sushi Go game.
This class represents a player in the game, managing their hand of cards,
played cards, and game state.
'''

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from sushigo.cards.card import Card
    from sushigo.game import Game


class Player:
    '''
    Represents a player in the game.
    '''

    def __init__(self, name: str):
        self.name = name
        self.hand: List[Card] = []
        self.played_cards: List[Card] = []
        self.wasabi_active: bool = False  # Track if Wasabi is active for this player
        self.maki_rolls: int = 0

    def add_card(self, card):
        """
        Adds a card to the player's hand.
        """
        self.hand.append(card)
        card.player = self

    def play_card(self, card):
        """
        Plays a card from the player's hand.
        """
        if card in self.hand:
            self.hand.remove(card)
            self.played_cards.append(card)
            card.on_play(self)
        else:
            raise ValueError(f"{card.name} is not in {self.name}'s hand.")

    def get_score(self, game: 'Game') -> int:
        """
        Calculates the player's score based on played cards.
        """
        score = 0
        for card in self.played_cards:
            score += card.get_value(self, game)
        return score
