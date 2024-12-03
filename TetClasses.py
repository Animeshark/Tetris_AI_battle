import pygame
import os
import random

# Define the Tetromino shapes and their associated images
SHAPE_ASSETS = {
    "yellow": "O.png",
    "line": "I.png",
    "green": "S.png",
    "blue": "J.png",
    "orange": "L.png",
    "purple": "T.png",
    "red": "Z.png"
}

# Scaling factors for all shapes and other assets
SHAPE_SCALE = (1, 1)
SIDEBAR_SCALE = (1, 1)
BOARD_SCALE = (1, 1)

# Load the images dynamically
TETROMINO_IMAGES = {}

for shape, filename in SHAPE_ASSETS.items():
    
    try:
        TETROMINO_IMAGES[shape] = [
            pygame.image.load(os.path.join(r"Tetris_assets/Shape Blocks", filename)), SHAPE_SCALE,
            pygame.image.load(os.path.join(r"Tetris_assets/Ghost", filename)), SHAPE_SCALE
        ]

    except FileNotFoundError as e:
        print(f"Error: File not found for shape '{shape}' - {e}")


# Load other assets
SIDEBAR = pygame.image.load(os.path.join("Tetris_assets", "sidebar.png"))
BOARD = pygame.image.load(os.path.join("Tetris_assets", "Board.png"))


BOARD_DIMES = (17, 11)




class tetris:
    def __init__(self, x: int, y: int, shape: str):
        self.x = x
        self.y = y
        self.origin = (x, y) #used to find rotation point
        self.shape = shape
        self.image = pygame.transform.scale(TETROMINO_IMAGES[self.shape][0], SHAPE_SCALE)
        self.ghost = pygame.transform.scale(TETROMINO_IMAGES[self.shape][1], SHAPE_SCALE)


    def draw(self, window) -> None:
        window.blit(self.image, (self.x, self.y))


    def draw_ghost(self, window, y) -> None:
        window.blit(self.ghost, (self.x, y))


class yellow(tetris):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "yellow")


class line(tetris):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "line")
        self.rotation = (x, y) # axis of rotation
    
    def rotate(self, direction: int) -> None:
        # direction 1 for left -1 for right
        self.image = pygame.transform.rotate(self.image, 90 * direction)
        # rotating self on the grid







class board:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        self.board = [] # Stores every dead shape in the board
        self.live = None # Current in play shape not stored in board

        self.grid = [[0 for _ in range(BOARD_DIMES[0])] for _ in range(BOARD_DIMES[1])] # Create empty boards using list comprehensions
        self.image = pygame.transform.scale(BOARD, BOARD_SCALE)
        self.width = self.image.get_width()
        self.length = self.image.get_height()
        self.sidebar = sidebar(x + self.width + 40, y)
        self.sidebar.fill()


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


    def fill(self) -> None:
        for i in range(6):
            self.addShape(i)

    def pop(self) -> None:

        for i in range(len(self.shapes) - 1):
            self.shapes[i] = self.shapes[i + 1]
            self.shapes[i].y = self.y + ((self.length//6) * i)

        self.addShape(-1)

    def addShape(self, index) -> None:
        shape = random.choice(list(SHAPE_ASSETS.keys()))
        self.shapes[index] = tetris(self.x + 10, self.y + ((self.length//6) * index), shape)




