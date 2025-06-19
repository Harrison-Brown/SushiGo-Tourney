from abc import ABC, abstractmethod

class Card(ABC):
    """
    Abstract base class for all cards in the game.
    """

    @abstractmethod
    def __init__(self, name: str, color:str):
        self.name = name
        self.color = color

    @abstractmethod
    def value(self) -> int:
        """
        Returns the value of the card.
        Will be based on board state
        """
        pass
