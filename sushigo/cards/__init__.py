from abc import ABC, abstractmethod
from sushigo.player import Player
from typing import Optional

class Card(ABC):
    """
    Abstract base class for all cards in the game.
    """

    @abstractmethod
    def __init__(self, name: str, color:str, player: Optional[Player] = None):
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
        return f"{self.name}({self.get_value()})"
    
    def __repr__(self):
        return f"{self.name}({self.get_value()})"