# -------- 10 Seconds To Midnight --------
# @compo Ludum Dare 27
# @theme 10 Seconds
# @author Gelatin Design, Laurence Roberts
# @date 24th - 25th August 2013
# ----------------------------------------

# -------- Init --------

# Load config
import app.Config

# Definitions

# Initialise pygame
import pygame
pygame.init( )

# Import app logic
from app.App import App
from app.Event import PygameEvent

# Create app
app.Config.app = App( )

# Setup the screen
app.Config.screen = pygame.display.set_mode( [app.Config.screen_w, app.Config.screen_h] )
pygame.display.set_caption( app.Config.app_title )
pygame.display.set_icon( pygame.image.load( "icon.png" ).convert_alpha( ) )
app.Config.screen.convert( )

# Create the clock
clock = pygame.time.Clock( )


# -------- Main Program Loop --------
while app.Config.app.running:

    # Capture events
    for pe in pygame.event.get( ):
        if app.Config.app.mode == "Menu":
            if pe.type == pygame.MOUSEBUTTONDOWN:
                app.Config.app.LoadGame( )
            elif pe.type == pygame.QUIT:
                app.Config.app.running = False
        else:
            event = PygameEvent( pe )
            app.Config.app.em.Post( event )

    # Process tick
    clock.tick( app.Config.fps )
    app.Config.app.Tick( clock.get_time() )


# -------- Exit --------
pygame.quit( )