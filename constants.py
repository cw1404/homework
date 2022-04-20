from pygame.locals import *

# Configuration of building shape block
# Width of the shape block
BWIDTH     = 50
# Height of the shape block
BHEIGHT    = 50
# Width of the line around the block
MESH_WIDTH = 3

# Configuration of the player board
# Board line height
BOARD_HEIGHT     = 7
# Margin of upper line (for score)
BOARD_UP_MARGIN  = 40
# Margins around all lines
BOARD_MARGIN     = 2

# Color declarations in the RGB notation
WHITE    = (255,255,255)
RED      = (230,10,10)
GREEN    = (10,220,10)
BLUE     = (20,30,200)
ORANGE   = (210,50,0)
GOLD     = (225,125,20)
PURPLE   = (120,20,100)
CYAN     = (0,200,200) 
BLACK    = (0,0,0)

# Timing constraints
# Time for the generation of TIME_MOVE_EVENT (ms)
MOVE_TICK          = 1000
# Allocated number for the move dowon event
TIMER_MOVE_EVENT   = USEREVENT+1
# Speed up ratio of the game (integer values)
GAME_SPEEDUP_RATIO = 1.5
# Score LEVEL - first threshold of the score
SCORE_LEVEL        = 2000
# Score level ratio
SCORE_LEVEL_RATIO  = 2 

# Configuration of score
# Number of points for one building block
POINT_VALUE       = 100
# Margin of the SCORE string
POINT_MARGIN      = 10

# Font size for all strings (score, pause, game over)
FONT_SIZE           = 25
