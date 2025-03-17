import pygame
import os

SCALE = 2.65


class Button:
    def __init__(self, cords: tuple, rest: str, hover: str):
        """
        cords: (x, y) coordinates, auto-centered.
        rest, hover: the sprites for when their cursor is over the button
        """

        self.rest_sprite = pygame.image.load(os.path.join("Tetris_assets\Buttons", rest))
        self.hover_sprite = pygame.image.load(os.path.join("Tetris_assets\Buttons", hover))
        
        # Pre-scale images 
        self.rest_sprite = pygame.transform.scale(self.rest_sprite, 
                                                  (self.rest_sprite.get_width() * SCALE, 
                                                   self.rest_sprite.get_height() * SCALE))
        self.hover_sprite = pygame.transform.scale(self.hover_sprite, 
                                                   (self.hover_sprite.get_width() * SCALE, 
                                                    self.hover_sprite.get_height() * SCALE))
        
        # Size after scaling
        self.width = self.rest_sprite.get_width()
        self.height = self.rest_sprite.get_height()

        self.x = cords[0] - self.width / 2
        self.y = cords[1] - self.height / 2

        # The difference in size between the two images
        self.image_dif = (self.hover_sprite.get_width() - self.width, self.hover_sprite.get_height() - self.height)

    def is_hovered(self) -> bool:

        """Check if the button is being hovered over."""
        mouse_pos = pygame.mouse.get_pos()
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height

    def draw(self, WINDOW) -> None:

        """Draw the button and change appearance on hover."""
        if self.is_hovered():
            WINDOW.blit(self.hover_sprite, (self.x, self.y))
        else:
            # Edits the drawing to account for change in size. Makes buttons scale from the origin
            WINDOW.blit(self.rest_sprite, (self.x + self.image_dif[0]/2, self.y + self.image_dif[1]/2))

    def is_clicked(self, previous_click) -> bool:
        
        """Check if the button is clicked."""

        if pygame.mouse.get_pressed()[0] and self.is_hovered() and previous_click == False:

            return True
        
        return False
    

class switch:

    def __init__(self, cords: tuple, rest: str, hover: str, switch_rest: str, switch_hover: str):
        super(Button).__init__(cords, rest, hover)

        self.switch_rest_sprite = pygame.image.load(os.path.join("Tetris_assets\Buttons", switch_rest))
        self.switch_hover_sprite = pygame.image.load(os.path.join("Tetris_assets\Buttons", switch_hover))

        self.switch_rest_sprite = pygame.transform.scale(self.switch_rest_sprite, 
                                                  (self.switch_rest_sprite.get_width() * SCALE, 
                                                   self.switch_rest_sprite.get_height() * SCALE))
        self.switch_hover_sprite = pygame.transform.scale(self.switch_hover_sprite, 
                                                   (self.switch_hover_sprite.get_width() * SCALE, 
                                                    self.switch_hover_sprite.get_height() * SCALE))
        
    def switch(self):
        self.switch_rest_sprite, self.rest_sprite = self.rest_sprite, self.switch_rest_sprite
        self.switch_hover_sprite, self.hover_sprite = self.hover_sprite, self.switch_hover_sprite
