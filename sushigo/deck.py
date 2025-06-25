from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List
import random

if TYPE_CHECKING:
    from sushigo.cards.card import Card  # Avoid circular import issues

class Deck(ABC):
    @abstractmethod
    def __init__(self, cards: List['Card']):
        # self.name = name
        self.cards = cards

    @abstractmethod
    def shuffle(self) -> None:
        """
        Shuffle the deck.
        """
        

    @abstractmethod
    def draw(self) -> 'Card':
        """
        Draw a card from the deck.
        """
        pass

    @abstractmethod
    def add_card(self, card: 'Card') -> None:
        """
        Add a card to the deck.
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Check if the deck is empty.
        """
        pass