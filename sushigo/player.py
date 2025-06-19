class Player():
    '''
    Represents a player in the game.
    '''
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.played_cards = []
        self.wasabi_active = False  # Track if Wasabi is active for this player

    def add_card(self, card):
        """
        Adds a card to the player's hand.
        """
        self.hand.append(card)
        card.player = self

    def play_card(self, card):
        """
        Plays a card from the player's hand.
        """
        if card in self.hand:
            self.hand.remove(card)
            self.played_cards.append(card)
            card.on_play(self)
        else:
            raise ValueError(f"{card.name} is not in {self.name}'s hand.")
    