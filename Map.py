import pygame
from pygame.locals import *

BROWN = (139,69,19) # Constant name for brown color.
class Map(pygame.sprite.Sprite): # Define class Map. Objects of this class include information about at which points the direction of an enemy should change.
    def __init__(self, number):
        super().__init__()
        self.number = number # The variable "number" is chosen according to the map the player chooses. This defines the path of the enemis.
        if self.number == 1:
            # Define a dictionary in which a certain point (intersection) in the field works as a key. The possible values in the dictionary are the following: "right", "left", "up", "down", "A", "B", "C", "D", "E" and "F". These control the direction of enemies. In cases "A", "B", "C", "D", "E" and "F" there are two possible directions to choose from and we choose randomly from these two.
            self.crit_points = {(0,348):"right", (204, 348):"up", (204, 96):"right", (498, 96):"down", (498,600):"right", (900,600):"up", (900, 498):"left", (798,498):"up", (798,150):"right", (1002,150):"up"}
            self.startx = 0 # X-coordinate of the beginning of the path of the enemies.
            self.starty = 348 # Y-coordinate of the beginning of the path of the enemies.
        elif self.number == 2:
            self.crit_points = {(0,100):"right", (200,100):"down", (200,300):"right", (500,300):"down", (500,550):"left", (400,550):"down", (400,650):"right", (1000,650):"up", (1000,500):"left", (850,500):"up", (850,400):"right", (1000,400):"up", (1000,250):"right", (1100,250):"up", (1100,100):"left", (900,100):"up"}
            self.startx = 0
            self.starty = 100
        elif number == 3:
            self.crit_points = {(550,700):"up", (550,600):"D", (300,600):"up", (800,600):"up", (800,500):"A", (300,450):"right", (800,450):"left", (550,450):"up", (1000,500):"up", (1000,270):"left", (550,270):"left", (200,270):"B", (200,100):"right", (250,100):"up", (100,270):"F", (100,500):"left"}
            self.startx = 550
            self.starty = 700
        elif number == 4:
            self.crit_points = {(600,700):"up", (600,600):"D", (300,600):"up", (900,600):"up", (300,400):"D", (900,400):"D", (1100,400):"up", (700,400):"up", (500,400):"up", (100,400):"up", (100,200):"B", (500,230):"right", (700,230):"left", (600,230):"up", (600,120):"D", (400,120):"up", (800,120):"up"}
            self.startx = 600
            self.starty = 700
    
    def get_crit_points(self):
        return self.crit_points
    
    def get_startx(self):
        return self.startx
    
    def get_starty(self):
        return self.starty
