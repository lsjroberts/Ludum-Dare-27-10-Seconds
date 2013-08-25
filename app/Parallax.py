# -------- Parallax.py --------
# Handles all logic relating to the world
# --------------------------

# Imports
import pygame, math
import Sprite


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
    tile = None
    tiles = []
    scroll_speed = 0
    repeat_y = False

    # -- Init --
    # 
    # @param Layer self
    # @param Sprite sprite
    # @return None
    def __init__( self, src, scroll_speed=None, repeat_y=None ):
        return
        self.tile = Tile( src, [0, 0] )

        if scroll_speed is None: scroll_speed = 0
        self.scroll_speed = int(scroll_speed)

        if repeat_y is None: repeat_y = False
        self.repeat_y = repeat_y

        self.count_x = int( math.ceil( float(Game.screen_width) / float(self.tile.rect.width) ) )
        if repeat_y:
            self.count_y = int( math.ceil( float(Game.screen_height) / float(self.tile.rect.height) ) )
        else:
            self.count_y = 1

        for x in range(0, count_x):
            for y in range(0, count_y):
                self.tiles.append(Tile(
                    src
                    [x*self.tile.rect.width, Config.screen_h - (y+1)*self.tile.rect.height]
                ))


    def Update( self ):
        far_left = Game.screen_width + 1
        far_right = -1

        for i in range(0, len(self.tiles)):
            self.tiles[i].pos[0] -= self.scroll_speed

            if self.tiles[i].pos[0] <  -self.tiles[i].rect.width:
                self.tiles[i].kill( )
                self.tiles[i].remove

            if self.tiles[i].pos[0] < far_left:
                far_left = self.tiles[i].pos[0]
            if self.tiles[i].pos[0] > far_right:
                far_right = self.tiles[i].pos[0]

            if far_left > 0:
                for y in range(0, self.count_y):
                    tile = copy.deepcopy(tile)
                    # tile.

                    self.tiles.append( Tile( [far_left - self.tile.rect.width, Game.screen_height - (y+1)*self.tile.rect.height], self.bgsrc, self.zindex ) )
                    Game.addSprite( "background", self.tiles[len(self.tiles)-1] )

            if far_right < Game.screen_width - self.tile.rect.width:
                for y in range(0, self.count_y):
                    #print self.bgsrc
                    self.tiles.append( Sprite( [far_right + self.tile.rect.width, Game.screen_height - (y+1)*self.tile.rect.height], self.bgsrc, self.zindex ) )
                    Game.addSprite( "background", self.tiles[len(self.tiles)-1] )


class Tile( Sprite.StaticSprite ):
    
    def __init__( self, src, pos ):
        self.groups = Config.app.sprite_groups['buildings'], Config.app.sprites_all
        Sprite.StaticSprite( self, src, pos )