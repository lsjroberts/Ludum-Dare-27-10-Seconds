# -------- Parallax.py --------
# Handles all logic relating to the world
# --------------------------

# Imports
import pygame, math


# -------- Background --------
class Background( ):
    layers = []

    # -- Init --
    # 
    # @param Background self
    # @param list layers
    # @return None
    def __init__( self, layers=None ):
        if layers is None: layers = []
        self.layers = layers


    # -- AddLayer --
    # 
    # @param Background self
    # @param Layer layer
    # @return None
    def AddLayer( self, layer ):
        self.layers.append( layer )



# -------- Layer --------
class Layer( ):
    sprite = None

    # -- Init --
    # 
    # @param Layer self
    # @param Sprite sprite
    # @return None
    def __init__( self, sprite, scroll_adjust=None, repeat_y=False ):
        self.SetSprite( sprite )

        if scoll_adjust is None: scroll_adjust = 0.0
        self.scroll_adjust = float(scroll_adjust)

        self.count_x = int( math.ceil( float(Game.screen_width) / float(self.tile.rect.width) ) )
        if repeat_y:
            self.count_y = int( math.ceil( float(Game.screen_height) / float(self.tile.rect.height) ) )
        else:
            self.count_y = 1


    # -- SetSprite --
    # 
    # @param Layer self
    # @param Sprite sprite
    # @return None
    def SetSprite( self, sprite ):
        self.sprite = sprite