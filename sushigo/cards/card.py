from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from sushigo.player import Player  # Avoid circular import issues
    from sushigo.game import Game  # Avoid circular import issues


class Card(ABC):
    default_count = 0

    @abstractmethod
    def __init__(
            self,
            name: str,
            color: str):
        self.name = name
        self.color = color

    @abstractmethod
    def get_value(self, player: 'Player', game: 'Game') -> int:
        """
        Returns the value of the card.
        Will be based on board state
        """
        pass

    @abstractmethod
    def on_play(self, player: 'Player', game: 'Game') -> None:
        """
        Called when the card is played.
        """
        pass

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__
