from sushigo.cards import Card
from sushigo.player import Player

class NigiriCard(Card):
    """
    Represents a Nigiri card.
    """
    color =  'yellow-orange'
    base_value = 0  
    name = '' 
    def __init__(self):
        super().__init__(self.name, self.color)
        self.value = self.base_value
    
    def on_play(self, player: Player):
        """
        When a Nigiri card is played, it adds its value to the player's score.
        If Wasabi is active, it modifies the value of the Nigiri card.
        """
        super().on_play(player)
        if player.wasabi_active:
            self.value = self.base_value * 3
            player.wasabi_active = False
        else:
            self.value = self.base_value

    def get_value(self) -> int:
        return self.value
    
class EggNigiriCard(NigiriCard):
    base_value = 1
    name = 'Egg Nigiri'
    
class SalmonNigiriCard(NigiriCard):
    base_value = 2
    name = 'Salmon Nigiri'
    
class SquidNigiriCard(NigiriCard):
    base_value = 3
    name = 'Squid Nigiri'