import pygame
from pygame.locals import *

BROWN = (139, 69, 19)
class Piece(pygame.sprite.Sprite): # Define a class "Piece". The objects of this class are pieces of the path of the enemies. The whole path of the enemies consists of these pieces.
    def __init__(self, x, y, xsize, ysize):
        super().__init__()
        self.image = pygame.Surface((xsize, ysize)) # Create a rectangular piece.
        self.image.fill(BROWN) # Paint the piece brown.
        self.rect = self.image.get_rect()
        self.rect.x = x # X-coordinate of the upper left corner of a piece.
        self.rect.y = y # Y-coordinate of the upper left corner of a piece.
        
