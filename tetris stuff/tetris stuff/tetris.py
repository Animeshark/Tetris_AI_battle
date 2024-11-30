import pygame
import os
import random

# Define the Tetromino shapes and their associated images
SHAPE_ASSETS = {
    "yellow": "square_shape.png",
    "line": "line_shape.png",
    "green": "left_squiggle.png",
    "blue": "right_L.png",
    "orange": "left_L.png",
    "purple": "T_shape.png",
    "red": "right_squiggle.png"
}

# Scaling factors for all shapes and other assets
SHAPE_SCALE = (1, 1)
SIDEBAR_SCALE = (1, 1)
BOARD_SCALE = (1, 1)

# Load the images dynamically
# TETROMINO_IMAGES = {shape: pygame.image.load(os.path.join("Tetris_assets", filename))
#                    for shape, filename in SHAPE_ASSETS.items()}

# Load other assets
SIDEBAR = pygame.image.load(os.path.join("Tetris_assets", "sidebar.png"))
BOARD = pygame.image.load(os.path.join("Tetris_assets", "board.png"))


BOARD_DIMES = (17, 11)




class tetris:
    def __init__(self, x: int, y: int, shape: str, image, scale: tuple):
        self.x = x
        self.y = y
        self.shape = shape
        self.image = pygame.transform.scale(image, scale)


    def draw(self, window):
        window.blit(self.img, (self.x, self.y))





class board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = []
        self.sidebar = sidebar()
        # Create empty boards using list comprehensions
        self.grid = [[0 for _ in range(BOARD_DIMES[0])] for _ in range(BOARD_DIMES[1])]
        
        self.image = pygame.transform.scale(BOARD, BOARD_SCALE)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

        for shape in self.board:
            shape.draw


class sidebar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(SIDEBAR, SIDEBAR_SCALE)
        self.shapes = []

    def fill_bar(self):
        for i in range(6):
            shape = random.choice(SHAPE_ASSETS)
            self.shapes.append()