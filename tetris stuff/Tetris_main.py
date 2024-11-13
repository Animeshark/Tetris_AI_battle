import pygame
import os
import random
import threading
from buttons import Button

pygame.font.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris AI")

main_menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("Tetris_assets", "menu_background.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 30
fps_lock = threading.Lock()   
clock = pygame.time.Clock()



def is_closed() -> bool:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return True

    
    return False


def draw_screen(bg, buttons: list) -> None:
   
        # Game logic, drawing etc.
        
        WINDOW.blit(bg, (0, 0))

        for button in buttons:
             button.draw_self(WINDOW)
        
        pygame.display.update()  # Update the window



def game_loop():
     return True


def options_screen() -> None:

    game_state = "options"

    screen_buttons = [Button((SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50),
                             ["start_button_rest.png", "start_button_hover.png"],
                              0.2, "game_state = main_menu") # Back button
                        ]
    
    WINDOW.fill((0, 0, 0))

    while game_state == "options":

        game_state = "exit" if is_closed() else game_state

        for button in screen_buttons:
            if button.is_clicked():
                button.execute()


        

        pygame.display.update()

    return False


def main_menu():

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

    while game_state == "main_menu":

        game_state = "exit" if is_closed() else game_state

        # Execute action when a button is clicked
        for button in screen_buttons:

            if button.is_clicked():

                button.execute()
                print(game_state)

        draw_screen(main_menu_bg, screen_buttons)  # Redraw the screen
        clock.tick(FPS)

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
            print("error")



    pygame.quit()


if __name__ == "__main__":
    main()