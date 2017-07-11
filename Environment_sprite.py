import pygame
from pygame.locals import *

class Environment(pygame.sprite.Sprite):
    def __init__(self, picture, x, y):
        super().__init__()
        self.image = picture # The picture of a texture.
        self.rect = self.image.get_rect()
        self.rect.x = x # X-coordinate of upper left corner of the picture.
        self.rect.y = y # y-coordinate of upper left corner of the picture.
