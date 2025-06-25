from sushigo.cards.card import Card
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sushigo.player import Player  # Avoid circular import issues
    from sushigo.game import Game  # Avoid circular import issues

class MakiRollCard(Card):
    """
    Represents a Maki Roll card.
    """
    color = 'red'
    rolls = 0

    def __init__(self):
        super().__init__(self.name, self.color)

    def on_play(self, player: 'Player', game: 'Game') -> None:
        """
        When a Maki Roll card is played, it adds to the player's Maki Rolls.
        """
        if player is None:
            raise ValueError("Player must be set before playing the card.")
        player.maki_rolls += self.rolls
        player.played_cards.append(self)

    def get_value(self, player: 'Player', game: 'Game') -> int:
        '''
        Based on who has the most Maki Rolls
        '''
        if player is None:
            raise ValueError(
                "Player must be set before getting the value of the card.")

        # if this isn't the most recent Maki roll, then 0
        if self != [c for c in player.played_cards if isinstance(
                c, MakiRollCard)][-1]:
            return 0

        roll_counts = sorted(
            list(set(p.maki_rolls for p in game.players)), reverse=True)

        prizes = [6, 3] if len(game.players) <= 5 else [6, 4, 2]
        for i, prize in enumerate(prizes):
            if len(
                    roll_counts) > i and player.maki_rolls == roll_counts[i]:
                return prize
        return 0


class MakiRoll1Card(MakiRollCard):
    rolls = 1
    name = 'Maki Roll 1'
    default_count = 4


class MakiRoll2Card(MakiRollCard):
    rolls = 2
    name = 'Maki Roll 2'
    default_count = 4


class MakiRoll3Card(MakiRollCard):
    rolls = 3
    name = 'Maki Roll 3'
    default_count = 4
