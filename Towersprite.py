import pygame
from pygame.locals import *

class Tower(pygame.sprite.Sprite): # Define a class Tower.
    def __init__(self):
        super().__init__()
        
    def update(self): # This methode is used when the player moves a tower around the field and is about to set the tower somewhere on the field.
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    

class Machine_gun_tower(Tower): # A class "Machine_gun_tower" that is a subclass of the class "Tower".
    def __init__(self, picture, beginning):
        super().__init__()
        self.image = picture # Picture is the image that represents a tower when it has been set to the game field.
        self.beginning = beginning # Beginning is the moment when the tower is set to the field.
        self.rect = self.image.get_rect()
        self.range = 100 # The range of a tower.
        self.interval = 0.22 # The time in seconds that a tower has to wait between two shots.
        self.damage = 15 # The damage a tower makes to an enemy.
        self.price = 350 # The price of a tower.
        self.poison = 0 # This defines whether the bullets that this tower shoots are poisonous or not. If self.poison = 0, bullets are not poisonous and if self.poison = 1, bullets are poisonous.
        self.type = 1 # This defines whether a tower is of type assistant or not. This is important becaus the bullets of an assistant-tower affect the enemy differently than bullets of other towers.
        self.type_2 = 1 # This variable defines wheter an enemy is immune to this type of tower.
        self.range_state = 0 # This variable is 0 if the range of this tower has not yet been updated. When range is updated, this is set to 1.
        self.rate_state = 0 # This variable is 0 if the shooting rate of this tower has not yet been updated. When shooting rate is updated, this is set to 1.
        self.damage_state = 0 # This variable is 0 if the damage of this tower has not yet been updated. When damage is updated, this is set to 1.
        self.poison_state = 0 # This variable is 0 if this tower has no poisoning property. When poisoning property is added, this is set to 1.
        self.PipeUp = 0 # This controls when the pipe of the tower is drawn to point upwards.
        self.x0 = 0 # X-coordinate of the endpoint of the pipe of the tower.
        self.y0 = 0 # Y-coordinate of the endpoint of the pipe of the tower.
        self.homing = 0 # Defines whether the tower shoots homing bullets or not.
        
class Homing_missile_tower(Tower):
    def __init__(self, picture, beginning):
        super().__init__()
        self.image = picture
        self.beginning = beginning
        self.rect = self.image.get_rect()
        self.range = 1000
        self.interval = 2.00
        self.damage = 250
        self.price = 500
        self.poison = 0
        self.type = 1
        self.type_2 = 6
        self.range_state = 0
        self.rate_state = 0
        self.damage_state = 0
        self.poison_state = 0
        self.PipeUp = 0
        self.x0 = 0
        self.y0 = 0
        self.homing = 1

class Shotgun_tower(Tower):
    def __init__(self, picture, beginning):
        super().__init__()
        self.image = picture
        self.beginning = beginning
        self.rect = self.image.get_rect()
        self.range = 100
        self.interval = 1.00
        self.damage = 170
        self.price = 450
        self.poison = 0
        self.type = 1
        self.type_2 = 4
        self.range_state = 0
        self.rate_state = 0
        self.damage_state = 0
        self.poison_state = 0
        self.PipeUp = 0
        self.x0 = 0
        self.y0 = 0
        self.homing = 0

class Assistant_tower(Tower):
    def __init__(self, picture, beginning):
        super().__init__()
        self.image = picture
        self.beginning = beginning
        self.rect = self.image.get_rect()
        self.range = 100
        self.interval = 1.10
        self.damage = 2
        self.price = 300
        self.poison = 0
        self.type = 2
        self.type_2 = 2
        self.range_state = 0
        self.rate_state = 0
        self.damage_state = 0
        self.poison_state = 0
        self.PipeUp = 0
        self.x0 = 0
        self.y0 = 0
        self.homing = 0

class Pistol_tower(Tower):
    def __init__(self, picture, beginning):
        super().__init__()
        self.image = picture
        self.beginning = beginning
        self.rect = self.image.get_rect()
        self.range = 100
        self.interval = 0.50
        self.damage = 10
        self.price = 200
        self.poison = 0
        self.type = 1
        self.type_2 = 3
        self.range_state = 0
        self.rate_state = 0
        self.damage_state = 0
        self.poison_state = 0
        self.PipeUp = 0
        self.x0 = 0
        self.y0 = 0
        self.homing = 0

class Mine(Tower):
    def __init__(self, picture):
        super().__init__()
        self.image = picture
        self.rect = self.image.get_rect()
        self.damage = 50
        self.price= 150
        self.range = 100

class Smart_bomb(Tower):
    def __init__(self, picture):
        super().__init__()
        self.image = picture
        self.rect = self.image.get_rect()
        self.damage = 80
        self.price = 300
        self.elist = [] # A list that contains the enemies within the range of a bomb.
        self.t = 0 # How long a red circle is drawn around a bomb when it explodes.
        self.number = 0
        self.range = 100
