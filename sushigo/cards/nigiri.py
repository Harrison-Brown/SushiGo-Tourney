from sushigo.cards.card import Card


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

    def on_play(self) -> None:
        """
        When a Nigiri card is played, it adds its value to the player's score.
        If Wasabi is active, it modifies the value of the Nigiri card.
        """
        if self.player is None:
            raise ValueError("Player must be set before playing the card.")
        if not hasattr(self.player, 'wasabi_active'):
            super().on_play()
            if self.player.wasabi_active:
                self.value = self.base_value * 3
                self.player.wasabi_active = False
            else:
                self.value = self.base_value

    def get_value(self) -> int:
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
