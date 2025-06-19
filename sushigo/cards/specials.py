'''
Special cards for Sushi Go game.
This module defines special cards like Wasabi, which have unique effects when played.
'''

from sushigo.cards.card import Card


class SpecialCard(Card):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)


class WasabiCard(SpecialCard):
    name = 'Wasabi'
    color = 'yellow-orange'
    default_count = 3

    def __init__(self):
        super().__init__(self.name, self.color)

    def get_value(self) -> int:
        return 0

    def on_play(self):
        if not self.player:
            raise ValueError("Wasabi must be played by a player.")
        self.player.wasabi_active = True
