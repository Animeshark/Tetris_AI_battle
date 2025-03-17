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
SIDEBAR = pygame.image.load(os.path.join("Tetris_assets", "Null.png"))
BOARD = pygame.image.load(os.path.join("Tetris_assets", "Board.png"))


BOARD_DIMES = (17, 11)




class tetris:
    def __init__(self, x: int, y: int, shape: str, rotation: tuple = None, x_: int = None, y_: int = None):
        self.x = x
        self.y = y
        self.shape = shape
        self.image = pygame.transform.scale(TETROMINO_IMAGES[self.shape][0], SHAPE_SCALE)
        self.ghost = pygame.transform.scale(TETROMINO_IMAGES[self.shape][1], SHAPE_SCALE)
        self.rotation = rotation
        self.grid = (x_, y_)


    def draw(self, window) -> None:
        window.blit(self.image, (self.x, self.y))


    def draw_ghost(self, window, y) -> None:
        window.blit(self.ghost, (self.x, y))

        
    def rotate(self, direction: int) -> None:
        """
        direction 1 for left -1 for right
        4 way rotation system
        """
        # resultant vector form rotation to top left
        result = (self.x - self.rotation[0], self.y - self.rotation[1])
        # rotating image
        self.image = pygame.transform.rotate(self.image, 90 * direction)
        # rotating vector
        result = (result[1] * -direction, result[0] * direction)
        self.x += result[0]
        self.y += result[1]




class yellow(tetris):
    def __init__(self, x: int, y: int, x_: int, y_: int):
        super().__init__(x, y, x_, y_, "yellow")


class line(tetris):
    def __init__(self, x: int, y: int, x_: int, y_: int):
        super().__init__(x, y, x_, y_, "yellow")
        # x and y are the top left corner
        #                          half a block to center on x          size of one block in y   +3 blocks - half a block to center on the 3rd block down
        self.rotation = (self.x + (self.image.get_width()//2), self.y + (self.image.get_height()//4) * 3 - (self.image.get_height()//4)//2) # axis of rotation
        self.state = True # true in upright pos

    def rotate(self, *args) -> None:
        """
        2 way rotation system
        Direction arguments are ignored
        """
        direction = 1 if self.state else -1
        # resultant vector form rotation to top left
        result = (self.x - self.rotation[0], self.y - self.rotation[1])
        # rotating image
        self.image = pygame.transform.rotate(self.image, 90 * direction)
        # rotating vector
        result = (result[1] * -direction, result[0] * direction)
        self.x += result[0]
        self.y += result[1]
        self.state = not self.state


        


        







class board:


    

    def __init__(self, x: int, y: int, hotkeys: dict):
        self.x = x
        self.y = y

        self.board = [] # Stores every dead shape in the board
        self.live = None # Current in play shape not stored in board

        self.grid = [[0 for _ in range(BOARD_DIMES[0])] for _ in range(BOARD_DIMES[1])] # Create empty boards using list comprehensions
        self.image = pygame.transform.scale(BOARD, BOARD_SCALE)

        self.width = self.image.get_width()
        self.length = self.image.get_height()

        # Create a semi-transparent black surface
        overlay = pygame.Surface((self.width, self.length))  # Same size as the screen
        overlay.set_alpha(102)  # 40% opacity (255 * 0.4 = 102)
        overlay.fill((0, 0, 0))  # Fill the surface with black

        self.sidebar = sidebar(x + self.width + 40, y)
        self.sidebar.fill()

        self.hotkeys = hotkeys

        self.alive = True
        self.cooldown = 30
        
        self.score = 0



    def draw(self, window) -> None:
        window.blit(self.img, (self.x, self.y))

        for shape in self.board:
            shape.draw(window)

        self.live.draw(window)      
        self.sidebar.draw(window)
    
        if self.alive:
            window.blit(self.overlay, (self.x, self.y))


    def roatate(self, direction) -> bool:
        """
        Returns true if rotated and false if not
        """
        self.live.rotate(direction)


    def step(input: dict) -> None:
        pass

    






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




