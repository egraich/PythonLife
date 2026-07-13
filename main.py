import pygame
import numpy as np

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 8
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

COLOR_BG = (10, 10, 15)
COLOR_ALIVE = (0, 255, 150)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("PythonLife")
clock = pygame.time.Clock()

grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.8, 0.2]).astype(np.int8)
paused = False

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
    screen.fill(COLOR_BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.size
            COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
            new_grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.8, 0.2]).astype(np.int8)
            r, c = min(grid.shape[0], ROWS), min(grid.shape[1], COLS)
            new_grid[:r, :c] = grid[:r, :c]
            grid = new_grid
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                pygame.display.set_caption(f"PythonLife {'[PAUSED]' if paused else ''}")

    pressed_buttons = pygame.mouse.get_pressed()
    if pressed_buttons[0] or pressed_buttons[2]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        col, row = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE
        if 0 <= col < COLS and 0 <= row < ROWS:
            grid[row, col] = 1 if pressed_buttons[0] else 0

    y_indices, x_indices = np.where(grid == 1)
    for row, col in zip(y_indices, x_indices):
        pygame.draw.rect(
            screen, 
            COLOR_ALIVE, 
            (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
        )

    if not paused:
        grid = update_grid(grid)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()