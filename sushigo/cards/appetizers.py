from sushigo.cards.card import Card

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sushigo.player import Player  # Avoid circular import issues
    from sushigo.game import Game  # Avoid circular import issues


class Appetizer(Card):
    """
    Base class for Appetizer cards in Sushi Go.
    Appetizers are worth 1 point each.
    """

    def __init__(self, name: str, color: str):
        super().__init__(name, color)


class TempuraCard(Appetizer):
    name = 'Tempura'
    default_count = 8
    color = 'light-pink'

    def __init__(self):
        super().__init__(self.name, self.color)

    def get_value(self, player: 'Player', game: 'Game') -> int:
        if player is None:
            raise ValueError(
                "Player must be set before getting the value of the card.")

        if player.played_cards.index(self) % 2 == 0:
            return 5

        return 0

    def on_play(self, player: 'Player', game: 'Game'):
        pass


class SashimiCard(Appetizer):
    name = 'Sashimi'
    default_count = 8
    color = 'bright-green'

    def __init__(self):
        super().__init__("Sashimi", "yellow")

    def get_value(self, player: 'Player', game: 'Game') -> int:
        if player is None:
            raise ValueError(
                "Player must be set before getting the value of the card.")

        if player.played_cards.index(self) % 3 == 0:
            return 5

        return 0

    def on_play(self, player: 'Player', game: 'Game'):
        pass
