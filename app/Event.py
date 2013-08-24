# -------- Event.py --------
# Handles event capturing, filtering and posting to listeners
# --------------------------

# -------- Event --------
# Superclass for any events that might be generated by an object and sent to
# the EventManager
class Event( ):
    name = "Generic Event"

    # -- Init --
    # Create the event object and set it's data
    # 
    # @param Event self
    # @param (optional) any data
    # @return Event self
    def __init__( self, data=None ):
        self.data = data



# -------- PygameEvent --------
# Pygame Event
class PygameEvent( Event ):
    name = "Pygame Event"


# -------- CollisionEvent --------
class CollisionEvent( Event ):
    name = "Collision Event"


# -------- Event Listener --------
# Superclass for any event listeners
class EventListener( ):

    # -- Init --
    # Create the event listener object
    # 
    # @param EventListener self
    # @return EventListener
    def __init__( self ):
        pass

    
    # -- Notify --
    # 
    # 
    # @param EventListener self
    # @return EventListener
    def Notify( self, event ):
        pass


# -------- Event Manager --------
# Responsible for coordinating events and communication between the models,
# views and controllers
class EventManager( ):

    # -- Init --
    # Create the event manager object
    # 
    # @param EventManager self
    # @return EventManager
    def __init__( self ):
        self.listeners = [ ]


    # -- Register Listener --
    # Append a new listener to the event manager
    #
    # @param EventManager self
    # @param EventListener listener
    # @return None
    def RegisterListener( self, listener ):
        for l in self.listeners:
            if l.__class__.__name__ == listener.__class__.__name__:
                return False

        self.listeners.append( listener )

    
    # -- Un-register Listener --
    # Remove a listener from the event manager
    #
    # @param EventManager self
    # @param EventListener listener
    # @return None
    def UnRegisterListener( self, listener ):
        pass


    # -- Post --
    # Post the event to all the registered listeners
    #
    # @param EventManager self
    # @param Event event
    # @return None
    def Post( self, event ):
        # Broadcast event to all listeners
        for listener in self.listeners:
            listener.Notify( event )