import pygame
import os

class Button:
    def __init__(self, cords: tuple, sprites: list, scale: int, func):
        """
        cords: (x, y) coordinates, auto-centered.
        sprites: list of 2 images [rest_sprite, hover_sprite].
        scale: scaling factor for the button size.
        func: function to execute when button is clicked.
        """
        self.scale = scale
        self.rest_sprite = pygame.image.load(os.path.join("Tetris_assets", sprites[0]))
        self.hover_sprite = pygame.image.load(os.path.join("Tetris_assets", sprites[1]))
        
        # Pre-scale images 
        self.rest_sprite = pygame.transform.scale(self.rest_sprite, 
                                                  (self.rest_sprite.get_width() * scale, 
                                                   self.rest_sprite.get_height() * scale))
        self.hover_sprite = pygame.transform.scale(self.hover_sprite, 
                                                   (self.hover_sprite.get_width() * scale, 
                                                    self.hover_sprite.get_height() * scale))
        
        self.width = self.rest_sprite.get_width()
        self.height = self.rest_sprite.get_height()
        self.x = cords[0] - self.width / 2
        self.y = cords[1] - self.height / 2
        self.func = func

    def is_hovered(self) -> bool:

        """Check if the button is being hovered over."""
        mouse_pos = pygame.mouse.get_pos()
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height

    def draw(self, WINDOW) -> None:

        """Draw the button and change appearance on hover."""
        if self.is_hovered():
            WINDOW.blit(self.hover_sprite, (self.x, self.y))
        else:
            WINDOW.blit(self.rest_sprite, (self.x, self.y))

    def is_clicked(self, previous_click) -> bool:
        
        """Check if the button is clicked."""

        if pygame.mouse.get_pressed()[0] and self.is_hovered() and previous_click == False:

            return True
        
        return False

    def execute(self) -> None:
        """Execute the assigned function or code string."""

        if callable(self.func):  # If it's a function, call it
            self.func()

        elif isinstance(self.func, str):  # If it's a string, execute the code
            exec(self.func)  # Note: exec() will execute the code as Python code
