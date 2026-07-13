import pygame
import numpy as np

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 8
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

COLOR_BG = (10, 10, 15)
COLOR_GRID = (20, 20, 30)
COLOR_DIE = (40, 40, 50)
COLOR_ALIVE = (0, 255, 150)

grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.8, 0.2]).astype(np.int8)

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

while 1:
    print(update_grid(grid))