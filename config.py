import pygame

# Window
DEFAULT_WIDTH = 800       # Initial window width in pixels
DEFAULT_HEIGHT = 600      # Initial window height in pixels
CELL_SIZE = 8             # Size of each grid cell in pixels (higher = bigger cells)
WINDOW_TITLE = "PythonLife"

# Colors
COLOR_BG = (10, 10, 15)        # Dark space background
COLOR_ALIVE = (0, 255, 150)    # Neon green for living cells

# Simulation Mechanics
BASE_FPS = 30                  # Default speed of the simulation (ticks per second)
SPAWN_ALIVE_CHANCE = 0.2       # Spawn density: 0.2 means 20% of the map fills with cells initially

# Speed Multipliers
MULT_SPEED_1 = 1               # Normal speed modifier
MULT_SPEED_2 = 2               # Fast speed modifier (by default 2x)
MULT_SPEED_3 = 4               # Super fast speed modifier (by default 4x)

# Input Bindings
KEY_PAUSE = pygame.K_SPACE     # Freeze/Unfreeze simulation
KEY_FULLSCREEN = pygame.K_F11  # Toggle borderless fullscreen
KEY_SPEED_1 = pygame.K_1       # Switch to normal speed
KEY_SPEED_2 = pygame.K_2       # Switch to fast speed
KEY_SPEED_3 = pygame.K_3       # Switch to super fast speed