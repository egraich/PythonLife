import pygame
import numpy as np

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 8  # Размер одной клетки в пикселях
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

COLOR_BG = (10, 10, 15)       # Тёмно-синий космос
COLOR_GRID = (20, 20, 30)     # Едва заметная сетка
COLOR_DIE = (40, 40, 50)      # Цвет следа (можно убрать)
COLOR_ALIVE = (0, 255, 150)   # Ядовито-зелёные живые клетки

