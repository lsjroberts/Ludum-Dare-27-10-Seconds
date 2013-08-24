# -------- Player.py --------
# Handles all logic relating to the Player
# ---------------------------

# Imports
import Sprite


# -------- Player --------
class Player( Sprite.MovingSprite ):
    max_speed = [100.0, 0.0]
    accl      = [100.0, 0.0]
    dccl      = [10.0,  0.0]


    # -- Init --
    #
    # @param Player self
    # @return None
    def __init__( self ):

        # Create as a MovingSprite
        Sprite.MovingSprite.__init__(
            self,
            "player.png",
            [0, 0]
        )

        # Add animation states
        self.AddAnimationState( "idle", 0, 3, 4 )
        self.AddAnimationState( "moving-right", 4, 7, 4 )
        self.AddAnimationState( "jumping", 8, 11, 4 )
        self.AddAnimationState( "falling", 12, 15, 4 )

        # Set to idle
        self.SetAnimationState( "idle" )

        # Register event listeners
        Config.app.em.RegisterListener( PlayerKeyboardListener() )

        # Register collisions
        self.AddCollider({
            'group': Config.app.sprite_groups['buildings'],
            'event': 'PlayerBuildingCollisionEvent',
            'callback': 'OnCollisionWithBuilding'
        })


    # -- OnCollisionWithBuilding --
    # 
    # @param Player self
    # @param Sprite c
    # @return None
    def OnCollisionWithBuilding( self, c ):
        pass


    # -- OnControlKeyDown --
    # 
    # @param Player self
    # @param Event event
    # @return None
    def OnControlKeyDown( self, event ):
        if event.key == self.control_JUMP:
            self.is_accl[1] = -1
            self.SetAnimationState( "jumping" )


    # -- OnControlKeyUp --
    # 
    # @param Player self
    # @param Event event
    # @return None
    def OnControlKeyUp( self, event ):
        pass



# -------- PlayerKeyboardListener --------
class PlayerKeyboardListener( EventListener ):
    
    def Notify( self, event ):
        if event.name == "Pygame Event":
            if event.data.type == pygame.KEYDOWN:
                Config.player.OnControlKeyDown( event.data )

            elif event.data.type == pygame.KEYUP:
                Config.player.OnControlKeyUp( event.data )