# -------- Config.py --------
# Shared configuration
# ---------------------------

# General Information
app_title = "10 Seconds To Midnight"
fps = 60
screen_w = 1024
screen_h = 768

# Sprite Layers
sprite_layer_player = 4
sprite_layer_computer = 3
sprite_layer_buildings = 2
sprite_layer_background = 1

# World
world_size = 4
world_offset = 0

# Colours
colour_player = (115, 241, 255)
colour_friendly = (111, 255, 0)
colour_enemy = (255, 0, 208)

# Shared Objects
app = None
screen = None
player = None
world = None

enemies = []