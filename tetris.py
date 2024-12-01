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
#TETROMINO_IMAGES = {shape: pygame.image.load(os.path.join("Tetris_assets", filename))
#                   for shape, filename in SHAPE_ASSETS.items()}

# Load other assets
#SIDEBAR = pygame.image.load(os.path.join("Tetris_assets", "sidebar.png"))
#BOARD = pygame.image.load(os.path.join("Tetris_assets", "board.png"))


BOARD_DIMES = (17, 11)




class tetris:
    def __init__(self, x: int, y: int, shape: str):
        self.x = x
        self.y = y
        self.shape = shape
        self.image = pygame.transform.scale(TETROMINO_IMAGES, SHAPE_SCALE)


    def draw(self, window) -> None:
        window.blit(self.img, (self.x, self.y))



class yellow(tetris):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "yellow")









class board:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.board = [] # Stores every shape in the board

        self.grid = [[0 for _ in range(BOARD_DIMES[0])] for _ in range(BOARD_DIMES[1])] # Create empty boards using list comprehensions

        self.image = pygame.transform.scale(BOARD, BOARD_SCALE)

        self.width = self.image.get_width()
        self.length = self.image.get_height()

        self.sidebar = sidebar(x + self.width + 40, y)


    def draw(self, window) -> None:
        window.blit(self.img, (self.x, self.y))

        for shape in self.board:
            shape.draw(window)
        
        self.sidebar.draw(window)





class sidebar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(SIDEBAR, SIDEBAR_SCALE)
        self.width = self.image.get_width()
        self.length = self.image.get_height()
        self.shapes = [] # Stores all shapes yet to come


    def fill_bar(self) -> None:

        for i in range(6):
            shape = random.choice(SHAPE_ASSETS)
            self.shapes.append(sidebarShape(self.x + 10, self.y + ((self.length//6) * i), shape))


class sidebarShape(tetris):
    def __init__(self, x: int, y: int, shape: str):
        super().__init__(x, y, shape)



print(SHAPE_ASSETS[random.randint(0, len(SHAPE_ASSETS))])