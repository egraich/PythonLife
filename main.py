import pygame
import numpy as np
import config

WIDTH, HEIGHT = config.DEFAULT_WIDTH, config.DEFAULT_HEIGHT
CELL_SIZE = config.CELL_SIZE
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(config.WINDOW_TITLE)
clock = pygame.time.Clock()

grid = np.random.choice(
    [0, 1], 
    size=(ROWS, COLS), 
    p=[1.0 - config.SPAWN_ALIVE_CHANCE, config.SPAWN_ALIVE_CHANCE]
).astype(np.int8)

paused = False
is_fullscreen = False
speed_multiplier = config.MULT_SPEED_1

def update_grid(current_grid):
    neighbors = (
        np.roll(current_grid, 1, axis=0) +
        np.roll(current_grid, -1, axis=0) +
        np.roll(current_grid, 1, axis=1) + 
        np.roll(current_grid, -1, axis=1) +
        np.roll(np.roll(current_grid, 1, axis=0), 1, axis=1) +
        np.roll(np.roll(current_grid, 1, axis=0), -1, axis=1) +
        np.roll(np.roll(current_grid, -1, axis=0), 1, axis=1) +
        np.roll(np.roll(current_grid, -1, axis=0), -1, axis=1)
    )
    birth = (neighbors == 3) & (current_grid == 0)
    survive = ((neighbors == 2) | (neighbors == 3)) & (current_grid == 1)
    return np.where(birth | survive, 1, 0).astype(np.int8)

running = True
while running:
    screen.fill(config.COLOR_BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:

            if not is_fullscreen:
                WIDTH, HEIGHT = event.size
                COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
                
                new_grid = np.random.choice(
                    [0, 1], 
                    size=(ROWS, COLS), 
                    p=[1.0 - config.SPAWN_ALIVE_CHANCE, config.SPAWN_ALIVE_CHANCE]
                ).astype(np.int8)
                r, c = min(grid.shape[0], ROWS), min(grid.shape[1], COLS)
                new_grid[:r, :c] = grid[:r, :c]
                grid = new_grid
                
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            if event.key == config.KEY_PAUSE:
                paused = not paused
                pygame.display.set_caption(f"{config.WINDOW_TITLE} {'[PAUSED]' if paused else ''}")
            elif event.key == config.KEY_FULLSCREEN:
                pygame.display.toggle_fullscreen()
                is_fullscreen = not is_fullscreen
                
                current_surface = pygame.display.get_surface()
                WIDTH, HEIGHT = current_surface.get_size()
                COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
                
                new_grid = np.random.choice(
                    [0, 1], 
                    size=(ROWS, COLS), 
                    p=[1.0 - config.SPAWN_ALIVE_CHANCE, config.SPAWN_ALIVE_CHANCE]
                ).astype(np.int8)
                r, c = min(grid.shape[0], ROWS), min(grid.shape[1], COLS)
                new_grid[:r, :c] = grid[:r, :c]
                grid = new_grid
            elif event.key == config.KEY_SPEED_1:
                speed_multiplier = config.MULT_SPEED_1
            elif event.key == config.KEY_SPEED_2:
                speed_multiplier = config.MULT_SPEED_2
            elif event.key == config.KEY_SPEED_3:
                speed_multiplier = config.MULT_SPEED_3

    if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        col, row = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE
        if 0 <= col < COLS and 0 <= row < ROWS:
            grid[row, col] = 1 if pygame.mouse.get_pressed()[0] else 0

    y_indices, x_indices = np.where(grid == 1)
    for row, col in zip(y_indices, x_indices):
        pygame.draw.rect(
            screen, 
            config.COLOR_ALIVE, 
            (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
        )

    if not paused:
        grid = update_grid(grid)

    pygame.display.flip()
    clock.tick(config.BASE_FPS * speed_multiplier)

pygame.quit()