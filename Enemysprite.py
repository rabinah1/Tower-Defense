import pygame
from pygame.locals import *
from Map import *
import random
import time

BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GRAY = (128,128,128)

# Load the pictures representing enemies of different colors.
red_monster = pygame.image.load("red_monster.jpg")
blue_monster = pygame.image.load("blue_monster.jpg")
black_monster = pygame.image.load("black_monster.jpg")
yellow_monster = pygame.image.load("yellow_monster.jpg")
gray_monster = pygame.image.load("gray_monster.jpg")

class Enemy(pygame.sprite.Sprite): # Define a class Enemy.
    def __init__(self, health, speed, price, color, resistant, points):
        super().__init__()
        self.color = color
        # Define the picture of an enemy.
        if (self.color == "black"):
            self.image = black_monster
        elif (self.color == "red"):
            self.image = red_monster
        elif (self.color == "blue"):
            self.image = blue_monster
        elif (self.color == "yellow"):
            self.image = yellow_monster
        elif (self.color == "gray"):
            self.image = gray_monster
        try:
            self.rect = self.image.get_rect()
        except AttributeError:
            print("Invalid enemy color!")
            import Main
            Main.main()
        self.health = health # The health of the enemy.
        self.value = 0 # A variable "value" that tells how long distance the enemy has travelled in the field.
        self.points = points  # A dictionary that contains the points in which the direction of the enemies should change and the directions to which the movement will change.
        self.direction = "none" # Initialize a variable that tells the direction of movement of the enemy.
        self.speed = speed # The speed of the enemy.
        self.n = 0 # A counter that ensures that an enemy chooses its direction only in an intersection and after it, the direction is kept constant.
        self.decideDirection = 0 # A variable that gets either value 0 or 1. This decides the direction of the enemy after an intersection.
        self.poisonTime = 0 # A counter that controls, how quickly poison affects the enemy.
        self.poison = 0 # A variable that tells whether an enemy is poisoned or not.
        self.price = price # The amount of money the player gets when he destroys this enemy.
        self.dist = 0 # The distnace of an enemy from a smart bomb.
        if (resistant == "none"):
            self.resistant = 5
        elif (resistant == "red"):
            self.resistant = 1
        elif (resistant == "blue"):
            self.resistant = 2
        elif (resistant == "yellow"):
            self.resistant = 3
        elif (resistant == "gray"):
            self.resistant = 4
        
    def get_location(self): # Returns the coordinates of an enemy.
        x = self.rect.centerx
        y = self.rect.centery
        coordinates = (x, y)
        return coordinates
    
    def update(self): # This controls, how the properties of an ememy (for example location) are varied within on iteration of a game loop.
        if self.poison == 1 and float(time.monotonic()) - float(self.poisonTime) > 3.0: # If the enemy is poisoned and over 3 seconds have passed since the poison last affected the enemy, we reduce the health of the enemy by 5.
            self.poisonTime = time.monotonic()
            self.health -= 5
            
        if self.get_location() in self.points: # If the coordinates of an enemy are the same as the coordinates of some intersection, we use these coordinates as a key to dictionary "self.points" and read the values corresponding to this key.
            self.n = 0
            self.direction = self.points[self.get_location()]
            
        if self.direction == "right": # If the dictionary returns a value "right", we move the enemy to the right with speed "self.speed" pixels / screen update.
            self.rect.centerx += self.speed
            
        elif self.direction == "left":
            self.rect.centerx -= self.speed
            
        elif self.direction == "up":
            self.rect.centery -= self.speed
            
        elif self.direction == "down":
            self.rect.centery += self.speed
            
        elif self.direction == "A": # If the dictionary returns a value "A", we choose randomly an integer from range [0,1] and depending on the result, we move the enemy to either up or right.
            if self.n == 0:
                self.decideDirection = random.randint(0,1)
                self.n = 1
            if self.decideDirection == 0:
                self.rect.centery -= self.speed
                self.direction = "up"
            elif self.decideDirection == 1:
                self.rect.centerx += self.speed
                self.direction = "right"
                
        elif self.direction == "B":
            if self.n == 0:
                self.decideDirection = random.randint(0,1)
                self.n = 1
            if self.decideDirection == 0:
                self.rect.centery -= self.speed
                self.direction = "up"
            elif self.decideDirection == 1:
                self.rect.centerx -= self.speed
                self.direction = "left"
                
        elif self.direction == "C":
            if self.n == 0:
                self.decideDirection = random.randint(0,1)
                self.n = 1
            if self.decideDirection == 0:
                self.rect.centery -= self.speed
                self.direction = "up"
            elif self.decideDirection == 1:
                self.rect.centery += self.speed
                self.direction = "down"
                
        elif self.direction == "D":
            if self.n == 0:
                self.decideDirection = random.randint(0,1)
                self.n = 1
            if self.decideDirection == 0:
                self.rect.centerx += self.speed
                self.direction = "right"
            elif self.decideDirection == 1:
                self.rect.centerx -= self.speed
                self.direction = "left"
                
        elif self.direction == "E":
            if self.n == 0:
                self.decideDirection = random.randint(0,1)
                self.n = 1
            if self.decideDirection == 0:
                self.rect.centerx += self.speed
                self.direction = "right"
            elif self.decideDirection == 1:
                self.rect.centery += self.speed
                self.direction = "down"
                
        elif self.direction == "F":
            if self.n == 0:
                self.decideDirection = random.randint(0,1)
                self.n = 1
            if self.decideDirection == 0:
                self.rect.centerx -= self.speed
                self.direction = "left"
            elif self.decideDirection == 1:
                self.rect.centery += self.speed
                self.direction = "down"

        self.value += self.speed
