from pygame.math import Vector2 as vec
#screen settings
WIDTH, HEIGHT = 610, 670
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH-TOP_BOTTOM_BUFFER, HEIGHT-TOP_BOTTOM_BUFFER
FPS = 60


#color settings
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255,255,255)
PLAYER_COLOR = (190, 194, 15)
#font settings
START_TEXT_SIZE = 19

START_FONT = 'arial black'
START_TEXT_STRING = 'PUSH SPACE BAR TO START'
#player settings

PLAYER_START_POS = vec(1,1)

#mob settings