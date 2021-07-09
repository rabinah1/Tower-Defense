import pygame
from pygame.locals import *

BROWN = (139, 69, 19)
class Piece(pygame.sprite.Sprite):
    def __init__(self, x, y, xsize, ysize):
        super().__init__()
        self.image = pygame.Surface((xsize, ysize))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
