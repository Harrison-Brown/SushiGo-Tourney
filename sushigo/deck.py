from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List, Type
import random
from sushigo.cards.card import Card
from sushigo.cards.appetizers import TempuraCard, SashimiCard, MisoSoupCard
from sushigo.cards.desserts import GreenTeaIceCreamCard
from sushigo.cards.nigiri import SquidNigiriCard, SalmonNigiriCard, EggNigiriCard
from sushigo.cards.rolls import MakiRoll1Card, MakiRoll2Card, MakiRoll3Card
from sushigo.cards.specials import TeaCard, WasabiCard


class Deck:
    card_list: List[Type[Card]] = []

    def __init__(self):
        self.cards = [
            card() for card in self.card_list for _ in range(  # type: ignore
                card.default_count)]
        self.shuffle()

    def shuffle(self) -> None:
        """
        Shuffle the deck.
        """
        random.shuffle(self.cards)

    def draw_cards(self, count: int = 1) -> List['Card']:
        """
        Draw a card from the deck.
        """
        if not self.cards:
            raise ValueError("Cannot draw from an empty deck.")
        if count > len(self.cards):
            raise ValueError("Not enough cards left in the deck.")
        return [self.cards.pop() for _ in range(count)]

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__


class FirstMealDeck(Deck):
    card_list = [
        TempuraCard,
        SashimiCard,
        MisoSoupCard,
        GreenTeaIceCreamCard,
        SquidNigiriCard,
        SalmonNigiriCard,
        EggNigiriCard,
        MakiRoll1Card,
        MakiRoll2Card,
        MakiRoll3Card,
        TeaCard,
        WasabiCard
    ]
