'''
Special cards for Sushi Go game.
This module defines special cards like Wasabi, which have unique effects when played.
'''

from sushigo.cards.card import Card
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sushigo.player import Player  # Avoid circular import issues
    from sushigo.game import Game  # Avoid circular import issues


class SpecialCard(Card):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)


class WasabiCard(SpecialCard):
    name = 'Wasabi'
    color = 'yellow-orange'
    default_count = 3

    def __init__(self):
        super().__init__(self.name, self.color)

    def get_value(self, player: 'Player', game: 'Game') -> int:
        return 0

    def on_play(self, player: 'Player', game: 'Game') -> None:
        """
        When a Wasabi card is played, it activates the Wasabi effect for the player.
        """
        if not player:
            raise ValueError("Wasabi must be played by a player.")
        player.wasabi_active = True
