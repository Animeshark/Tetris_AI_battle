import pygame
import os
import random
import TetClasses
from buttons import *

pygame.font.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris AI")
HOTKEYS = {
    "P1":{
        "anti_clockwise": pygame.K_a,
        "clockwise": pygame.K_d,
        "hard_down": pygame.K_s,
        "soft_down": pygame.K_w,
        "hold": pygame.K_e
    },
    "P2":{
        "anti_clockwise": pygame.K_l,
        "clockwise": pygame.K_j,
        "hard_down": pygame.K_k,
        "soft_down": pygame.K_i,
        "hold": pygame.K_o  
    }
}


FPS = 30
clock = pygame.time.Clock()
training = False
players = 1
loss_font = pygame.font.SysFont("comicsans", 50)


def is_closed() -> bool:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return True

    
    return False


def Compute(board) -> dict:
    pass





def game_loop():
    
    bg = pygame.transform.scale(pygame.image.load(os.path.join("Tetris_assets", "menu_background.png")), (SCREEN_HEIGHT, SCREEN_WIDTH))

    def draw_screen(boards: list):
         
        WINDOW.blit(bg, (0,0))

        for board in boards:
            board.draw(WINDOW)

        pygame.display.update()

   

    
    #Initialising
    game_state = "game_loop"

    WINDOW.fill((0, 0, 0))

    # Create empty boards for player and AI
        
    playing = True
    while playing:

        keys = pygame.key.get_pressed()

        # Checks if user closed window
        playing = is_closed()




        # Steps boards




        clock.tick(FPS)

            

            





def options_screen() -> None:

    WINDOW.fill((0, 0, 0))

    game_state = "options"
    leftdown = True
    options_screen_bg = pygame.transform.scale(pygame.image.load(os.path.join("Tetris_assets", "menu_background.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))

    back = Button((0 + 120, SCREEN_HEIGHT - 60),
                             "back_button_rest.png", "back_button_hover.png",
    ) # Back button
    
    exit = Button((SCREEN_WIDTH - 120, SCREEN_HEIGHT - 60),
                "exit_button_rest.png", "exit_button_hover.png")  # Exit button
    

    screen_buttons = [back, exit]
    


    def draw_screen(bg, buttons: list) -> None:
   
        # Game logic, drawing etc.
        
        WINDOW.blit(bg, (0, 0))

        for button in buttons:
            button.draw(WINDOW)
        
        pygame.display.update()  # Update the window

    while game_state == "options":

        game_state = "exit" if is_closed() else game_state

        if back.is_clicked(leftdown):
            game_state = 'main_menu'

        elif exit.is_clicked(leftdown):
            game_state = 'exit'

        leftdown = pygame.mouse.get_pressed()[0]
        







        draw_screen(options_screen_bg, screen_buttons)

    return game_state


def main_menu():

    WINDOW.fill((0, 0, 0))


    main_menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("Tetris_assets", "menu_background.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = 'main_menu'

    
    start = Button((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                "start_button_rest.png", "start_button_hover.png") # Start button

    options = Button((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120),
                "option_button_rest.png", "option_button_hover.png") # Options button

    exit = Button((SCREEN_WIDTH - 120, SCREEN_HEIGHT - 60),
                "exit_button_rest.png", "exit_button_hover.png")  # Exit button
    
    screen_buttons = [start, options, exit]
    leftdown = True #remembers if mouse was clicked in previous frame

    def draw_screen(bg, buttons: list) -> None:
   
        # Game logic, drawing etc.
        
        WINDOW.blit(bg, (0, 0))
        for button in buttons:
            button.draw(WINDOW)
        
        pygame.display.update()  # Update the window

    while game_state == "main_menu":
        
        game_state = "exit" if is_closed() else game_state # checks if the window is closed

        # Execute action when a button is clicked
        if start.is_clicked(leftdown):
            game_state = 'game_loop'

        elif options.is_clicked(leftdown):
            game_state = 'options'

        elif exit.is_clicked(leftdown):
            game_state = 'exit'

        leftdown = pygame.mouse.get_pressed()[0]






        draw_screen(main_menu_bg, screen_buttons)  # Redraw the screen
        clock.tick(FPS)

    return game_state  # End the game


def main():
    run = True
    game_state = "main_menu"  # Game state to track which screen is active
    
    while run:

        run != is_closed()
       

        if game_state == "main_menu":
            game_state = main_menu()  # Run the main menu and change game state on button click

        elif game_state == "game_loop":
            game_state = game_loop()  # Start the game loop and switch state after the game

        elif game_state == "options":
            game_state = options_screen()  # Show the options screen and switch state after

        elif game_state == "exit":
            run = False
        
        else:
            print("game_state error")
            pygame.quit()



    pygame.quit()



if __name__ == "__main__":
    main()


