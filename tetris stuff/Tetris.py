import pygame
import random

pygame.init()

#CONSTANTS

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BLOCK_SIZE = 30
SHAPES = [
    [[[1, 1, 1],  
      [0, 1, 0]],  
      
     [[0,1],
      [1,1],
      [0,1]],
      
     [[0, 1, 0],
      [1, 1, 1]],
      
     [[1,0],
      [1,1],
      [1,0]]],

    [[[0, 2, 2],
      [2, 2, 0]],
    
     [[2,0],
      [2,2],
      [0,2]]],

    [[[3, 3, 0],
      [0, 3, 3]],

     [[0,3],
      [3,3],
      [3,0]]],

    [[[4, 0, 0],
      [4, 4, 4]],

     [[4,4],
      [4,0],
      [4,0]],
     
     [[4,4,4],
      [0,0,4]],

     [[0,4],
      [0,4],
      [4,4]]],

    [[[0, 0, 5],
      [5, 5, 5]],

     [[5,0],
      [5,0],
      [5,5]],

     [[5, 5, 5],
      [5, 5, 5]],

     [[5,5],
      [0,5],
      [0,5]]],

    [[[6, 6],
      [6, 6]]],

    [[[7, 7, 7, 7]],

     [[7],
      [7],
      [7],
      [7],]]

]

#IMAGES

backImage = "Placeholder"

#CONTROLS

rotateL = "LEFT_ARROW"
rotateR = "RIGHT_ARROW"
dragdown = "DOWN_ARROW"
    
#BOARD

PlayerBoard = [         
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0]
            ]


#TETRINOMS

class tetris:
    def __init__(self, shape: list, code: int, x: int, y: int):
        self.rotation = 0
        self.x = x
        self.y = y
        self.shape = shape
        self.code = code

    def rotate(self, direction: str):
        if direction == "left":
            self.rotation -= 1
        elif direction == "right":
            self.rotation += 1
        else:
            print("Wrong rotation")
        if self.rotation % 4 == 0:
            self.rotation = 0

    def draw(self, board: list):
        gold = True
        #Checking for space
        for y in range(len(self.shape[self.rotation])):
            for x in range(len(self.shape[self.rotation][y])):
                if self.shape[self.rotation][y][x] == self.code:
                    if board[y + self.y][x + self.x] != 0:
                        gold = False
                        return False
                        

        #Puting piece in space
        if gold == True:
            for y in range(len(self.shape[self.rotation])):
                for x in range(len(self.shape[self.rotation][y])):
                    if self.shape[self.rotation][y][x] == self.code:
                        board[y + self.y][x + self.x] = self.code
                        return True

    def lower_self(self, board: list):
        self.y -= 1
        if tetris.draw(board) == False:
            self.y += 1
            return False
        else:
            return True
        
    def shape_locked(self, board: list):
        for row in range(len(board)):
            if row >= self.y:
                for pos in range(len(board[row])):
                    if pos >= self.x:
                        if board[row][pos] == self.code:
                            board[row][pos] += 7
            
            



def spawn_shape(piece: int, board: list):
        center = 5 - (len(SHAPES[piece - 1][0])//2)
        shape = tetris(SHAPES[piece - 1],piece,center,0)
        shape.draw(board)
        return shape

def swap_rows(board: list, rows: list):
        index = -1
        while rows[index] > rows[0]:
            board[rows[index]], board[rows[index] - 1] = board[rows[index] - 1], board[rows[index]]
            index -= 1
        

def clear_layer(board: list):
            empty_rows = []
            BOARD_WIDTH = len(board[0])
            BOARD_HEIGHT = len(board)
            top = 0
            line_empty = 0
            for row in range(BOARD_HEIGHT):
                for pos in range(BOARD_WIDTH):
                    if board[row][pos] > 7:
                        clear = True
                        line_empty += 1
                    else:
                        clear = False
                        break

                if line_empty == BOARD_WIDTH:
                    top = row

                if clear == True:
                    for pos in range(len(board[row])):
                        board[row][pos] == 0
                    empty_rows.append(row)
                    
            empty_rows.insert(0, top)
            swap_rows(board, empty_rows)
            
            
                



         
                            
                            




    
#WINDOW

def background(image):
    size = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(size, (0,0))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#GAME_LOOP

difficulty = 10
run = True

def player():
    piece = tetris()

    while run:

        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN(rotateL):
                piece.rotate("left")

        keys = pygame.key.get_pressed()


        pygame.display.update()



            

    pygame.quit()