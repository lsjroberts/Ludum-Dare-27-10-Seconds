# -------- Building.py --------
# Handles all logic relating to the Buildings
# ---------------------------

# Imports
import Config, Sprite


# -------- Building --------
class Building( Sprite.StaticSprite ):
    
    # -- Init --
    # 
    # @param Building self
    # @return None
    def __init__( self, pos ):

        # Set group
        self.groups = Config.app.sprite_groups["buildings"], Config.app.sprites_all

        # Set layer
        self._layer = Config.sprite_layer_buildings

        # Create as a StaticSprite
        Sprite.StaticSprite.__init__(
            self,
            "building.png",
            pos
        )
