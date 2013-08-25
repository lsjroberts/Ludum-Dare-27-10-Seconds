# -------- World.py --------
# Handles all logic relating to the world
# --------------------------

# Imports
import random
import Config, Parallax, Building, Computer


# -------- World --------
class World( ):
    background = None
    buildings = []
    computer = None

    # -- Init --
    # 
    # @param World self
    # @return World
    def __init__( self ):
        self.styles = [ "green" ]
        self.Generate( )


    # -- Generate --
    #
    # @param World self
    # @return None
    def Generate( self, difficulty=1 ):
        style = random.choice( self.styles )

        self.background = Parallax.Background([
            "worlds/" + style + "/background-fore.png",
            "worlds/" + style + "/background-middle.png",
            "worlds/" + style + "/background-far.png",
            "worlds/" + style + "/background-back.png"
        ])

        building_size_x = 350
        building_size_y = 600

        distance_x = difficulty * 200
        distance_y = difficulty * 20

        center = int( Config.screen_w / 2 )
        left_x = center - distance_x - building_size_x
        left_y = int( Config.screen_h / 2 )
        right_x = center + distance_x
        right_y = left_y + distance_y

        self.buildings.append( Building.Building([left_x, left_y]) )
        self.buildings.append( Building.Building([right_x, right_y]) )

        self.computer = Computer.Computer([right_x + building_size_x - 80, right_y - 28])