# -------- Computer.py --------
# Handles all logic relating to the Computer
# ---------------------------

# Imports
import Config, Sprite


# -------- Computer --------
class Computer( Sprite.StaticSprite ):
    
    # -- Init --
    # 
    # @param Computer self
    # @return None
    def __init__( self, pos ):

        # Set group
        self.groups = Config.app.sprite_groups["computer"], Config.app.sprites_all

        # Set layer
        self._layer = Config.sprite_layer_computer

        # Create as a StaticSprite
        Sprite.StaticSprite.__init__(
            self,
            "computer.png",
            pos
        )
