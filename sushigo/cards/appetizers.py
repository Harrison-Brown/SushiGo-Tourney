from sushigo.cards.card import Card


class Appetizer(Card):
    """
    Base class for Appetizer cards in Sushi Go.
    Appetizers are worth 1 point each.
    """


class Tempura(Appetizer):
    def __init__(self, player=None):
        super().__init__("Tempura", "yellow", player)

    def get_value(self) -> int:
        if self.player is None:
            raise ValueError(
                "Player must be set before getting the value of the card.")

        if self.player.played_cards.index(self) % 2 == 0:
            return 5

        return 0

    def on_play(self):
        pass


class Sashimi(Appetizer):
    def __init__(self, player=None):
        super().__init__("Sashimi", "yellow", player)

    def get_value(self) -> int:
        if self.player is None:
            raise ValueError(
                "Player must be set before getting the value of the card.")

        if self.player.played_cards.index(self) % 3 == 0:
            return 5

        return 0

    def on_play(self):
        pass
