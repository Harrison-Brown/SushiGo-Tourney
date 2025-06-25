from sushigo.cards.card import Card
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sushigo.player import Player  # Avoid circular import issues
    from sushigo.game import Game  # Avoid circular import issues

class NigiriCard(Card):
    """
    Represents a Nigiri card.
    """
    color = 'yellow-orange'
    base_value = 0
    name = ''

    def __init__(self):
        super().__init__(self.name, self.color)
        self.value = self.base_value

    def on_play(self, player: 'Player', game: 'Game') -> None:
        """
        When a Nigiri card is played, it adds its value to the player's score.
        If Wasabi is active, it modifies the value of the Nigiri card.
        """
        if player is None:
            raise ValueError("Player must be set before playing the card.")
        if not hasattr(player, 'wasabi_active'):
            super().on_play(player, game)
            if player.wasabi_active:
                self.value = self.base_value * 3
                player.wasabi_active = False
            else:
                self.value = self.base_value

    def get_value(self, player: 'Player', game: 'Game') -> int:
        return self.value


class EggNigiriCard(NigiriCard):
    base_value = 1
    name = 'Egg Nigiri'
    default_count = 4


class SalmonNigiriCard(NigiriCard):
    base_value = 2
    name = 'Salmon Nigiri'
    default_count = 5


class SquidNigiriCard(NigiriCard):
    base_value = 3
    name = 'Squid Nigiri'
    default_count = 3
