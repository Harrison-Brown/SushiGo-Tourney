from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from sushigo.player import Player  # Avoid circular import issues


class Card(ABC):
    @abstractmethod
    def __init__(
            self,
            name: str,
            color: str,
            player: Optional['Player'] = None):
        self.name = name
        self.color = color
        self.player = player

    @abstractmethod
    def get_value(self) -> int:
        """
        Returns the value of the card.
        Will be based on board state
        """
        pass

    @abstractmethod
    def on_play(self):
        """
        Called when the card is played.
        """
        pass

    def __str__(self):
        try:
            return f"{self.name}({self.get_value()})"
        except ValueError:
            return f"{self.name}(N/A)"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.color})"
