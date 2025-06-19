from sushigo.cards import Card

class SpecialCard(Card):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

class WasabiCard(SpecialCard):
    name = 'Wasabi'
    color = 'yellow-orange'
    def __init__(self):
        super().__init__(self.name, self.color)
    
    def get_value(self) -> int:
        return 0
    
    def on_play(self, player):
        player.wasabi_active = True
