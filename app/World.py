# -------- World.py --------
# Handles all logic relating to the world
# --------------------------

# Imports
import Parallax


# -------- World --------
class World( ):
    background = None

    # -- Init --
    # 
    # @param World self
    # @return World
    def __init__( self ):
        self.background = Parallax.Background()
