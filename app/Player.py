# -------- Player.py --------
# Handles all logic relating to the Player
# ---------------------------

# Imports
import pygame
import Config, Event, Sprite


# -------- Player --------
class Player( Sprite.PhysicsSprite ):
    max_speed = [400.0, 400.0]
    accl      = [100.0, 100.0]
    dccl      = [100.0,  20.0]

    control_ACTION = pygame.K_SPACE


    # -- Init --
    #
    # @param Player self
    # @return None
    def __init__( self ):

        # Set group
        self.groups = Config.app.sprite_groups["player"], Config.app.sprites_all

        # Set layer
        self._layer = Config.sprite_layer_player

        building = Config.world.buildings[0]

        # Create as a MovingSprite
        Sprite.MovingSprite.__init__(
            self,
            "player.png",
            [building.rect.x + 40, building.rect.y - 40]
        )

        # Add animation states
        self.AddAnimationState( "idle", 0, 0, 1 )
        # self.AddAnimationState( "idle", 0, 3, 4 )
        # self.AddAnimationState( "moving-right", 4, 7, 4 )
        # self.AddAnimationState( "jumping", 8, 11, 4 )
        # self.AddAnimationState( "falling", 12, 15, 4 )

        # Set to idle
        self.SetAnimationState( "idle" )

        # Register event listeners
        Config.app.em.RegisterListener( PlayerKeyboardListener() )

        # Register colliders
        self.AddCollider({
            'group': Config.app.sprite_groups['buildings'],
            'event': 'PlayerBuildingCollisionEvent',
            'callback': 'OnCollisionWithBuilding',
            'false_callback': 'OnNotCollisionWithBuilding'
        })

        self.AddCollider({
            'group': Config.app.sprite_groups['computer'],
            'event': 'PlayerComputerCollisionEvent',
            'callback': 'OnCollisionWithComputer',
            'false_callback': 'OnNotCollisionWithComputer'
        })


    # -- OnCollisionWithBuilding --
    # 
    # @param Player self
    # @param Sprite c
    # @return None
    def OnCollisionWithBuilding( self, c ):
        # If the building is below the player
        if c.rect.y >= self.rect.y:
            self.is_falling = False
        else:
            self.is_accl[0] = 0
            self.cur_speed[0] = 0


    # -- OnNotCollisionWithBuilding --
    # 
    # @param Player self
    # @return None
    def OnNotCollisionWithBuilding( self ):
        self.is_falling = True


    # -- OnCollisionWithComputer --
    # 
    # @param Player self
    # @param Sprite c
    # @return None
    def OnCollisionWithComputer( self, c ):
        self.is_accl[0] = 0
        self.cur_speed[0] = 0


    # -- OnNotCollisionWithComputer --
    # 
    # @param Player self
    # @return None
    def OnNotCollisionWithComputer( self ):
        pass


    # -- OnControlKeyDown --
    # 
    # @param Player self
    # @param Event event
    # @return None
    def OnControlKeyDown( self, event ):
        # First press of spacebar makes the player run
        if self.cur_speed[0] == 0 and event.key == self.control_ACTION:
            self.is_accl[0] = 1

        # Second press of spacebar makes the player jump
        elif self.is_falling == False and event.key == self.control_ACTION:
            self.is_accl[1] = -1
            # self.SetAnimationState( "jumping" )


    # -- OnControlKeyUp --
    # 
    # @param Player self
    # @param Event event
    # @return None
    def OnControlKeyUp( self, event ):
        # When the player lets go of the spacebar, stop jumping
        if self.is_falling == False and event.key == self.control_ACTION:
            self.is_accl[1] = 0



# -------- PlayerKeyboardListener --------
class PlayerKeyboardListener( Event.EventListener ):
    
    def Notify( self, event ):
        if event.name == "Pygame Event":
            if event.data.type == pygame.KEYDOWN:
                Config.player.OnControlKeyDown( event.data )

            elif event.data.type == pygame.KEYUP:
                Config.player.OnControlKeyUp( event.data )