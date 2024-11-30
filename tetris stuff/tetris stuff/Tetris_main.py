import pygame
import os
import random
import tetris
from buttons import Button

pygame.font.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris AI")


FPS = 30
clock = pygame.time.Clock()
training = False
players = 1


def is_closed() -> bool:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return True

    
    return False


def check_buttons(buttons: list, previous_mouse_state) -> None:
    for button in buttons:

        if button.is_clicked(previous_mouse_state):

            button.execute()



def game_loop():
     
     def draw_screen(bg, boards: list):
         
         WINDOW.blit(bg, (0,0))

         for board in boards:
             board.draw(WINDOW)

        

     
     if training == False:
        #Initialising
        game_state = "game_loop"

        WINDOW.fill((0, 0, 0))

        boards = []

        if players == 1:
            
            # Create empty boards for player and AI
            PlayerBoard = tetris.board(200, 700)
            Ai_board = tetris.board(800, 700)

            boards.append(PlayerBoard, Ai_board)

            






     
     else:
         pass


def options_screen() -> None:

    WINDOW.fill((0, 0, 0))

    game_state = "options"
    mouse = True
    options_screen_bg = pygame.transform.scale(pygame.image.load(os.path.join("Tetris_assets", "menu_background.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))

    screen_buttons = [Button((SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50),
                             ["start_button_rest.png", "start_button_hover.png"],
                              0.2, "game_state = main_menu") # Back button
                        ]
    


    def draw_screen(bg, buttons: list) -> None:
   
        # Game logic, drawing etc.
        
        WINDOW.blit(bg, (0, 0))

        for button in buttons:
            button.draw(WINDOW)
        
        pygame.display.update()  # Update the window

    while game_state == "options":

        game_state = "exit" if is_closed() else game_state

        check_buttons(screen_buttons, mouse)


        

        draw_screen(options_screen_bg, screen_buttons)

    return game_state


def main_menu():

    WINDOW.fill((0, 0, 0))


    main_menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("Tetris_assets", "menu_background.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = 'main_menu'

    screen_buttons = [
        Button((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                ["start_button_rest.png", "start_button_hover.png"],
                  0.2, "game_state = 'game_loop'"), # Start button

        Button((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120),
                ["start_button_rest.png", "start_button_hover.png"],
                  0.2, "game_state = 'options_screen'"), # Options button

        Button((SCREEN_WIDTH - 120, SCREEN_HEIGHT - 60),
                ["start_button_rest.png", "start_button_hover.png"],
                  0.2, "game_state = 'exit'")  # Exit button
    ]

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
        check_buttons(screen_buttons, leftdown)


        draw_screen(main_menu_bg, screen_buttons)  # Redraw the screen
        clock.tick(FPS)

        leftdown = pygame.mouse.get_pressed()[0] #checks if left button is clicked

    return game_state  # End the game

def main():
    run = True
    game_state = "main_menu"  # Game state to track which screen is active
    
    while run:

        run = is_closed()

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

if __name__ == "__main__":
    main()


