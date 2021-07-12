import pygame
import random
import time
from common import (red_monster, blue_monster, black_monster,
                    yellow_monster, gray_monster)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, speed, price, color, immunity, points):
        super().__init__()
        self.color = color
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
        self.health = health
        self.travelled = 0  # Tells how long distance the enemy has travelled in the field.
        # A dictionary that contains the points in which the direction of the enemies should
        # change and the directions to which the movement will change.
        self.points = points
        self.direction = "none"
        self.speed = speed
        # select_direction ensures that an enemy chooses its direction only in an intersection
        # and after it, the direction is kept constant.
        self.select_direction = False
        self.get_direction = 0
        self.poison_time = 0  # How quickly poison affects the enemy.
        self.poison = 0
        self.price = price  # The amount of money the player gets when the enemy is destroyed
        self.dist = 0  # The distnace of an enemy from a smart bomb
        if (immunity == "none"):
            self.immunity = 5
        elif (immunity == "red"):
            self.immunity = 1
        elif (immunity == "blue"):
            self.immunity = 2
        elif (immunity == "yellow"):
            self.immunity = 3
        elif (immunity == "gray"):
            self.immunity = 4

    def get_location(self):
        x = self.rect.centerx
        y = self.rect.centery
        coordinates = (x, y)
        return coordinates

    def update(self):
        if self.poison == 1 and float(time.monotonic()) - float(self.poison_time) > 3.0:
            self.poison_time = time.monotonic()
            self.health -= 5

        # Coordinates of an enemy are the same as the coordinates of some intersection
        if self.get_location() in self.points:
            self.select_direction = True
            self.direction = self.points[self.get_location()]

        if self.direction == "right":
            self.rect.centerx += self.speed

        elif self.direction == "left":
            self.rect.centerx -= self.speed

        elif self.direction == "up":
            self.rect.centery -= self.speed

        elif self.direction == "down":
            self.rect.centery += self.speed

        # If the dictionary returns a value "A", choose randomly an integer from range
        # [0,1] and depending on the result, move the enemy to either up or right.
        elif self.direction == "A":
            if self.select_direction:
                self.get_direction = random.randint(0, 1)
                self.select_direction = False
            if self.get_direction == 0:
                self.rect.centery -= self.speed
                self.direction = "up"
            elif self.get_direction == 1:
                self.rect.centerx += self.speed
                self.direction = "right"

        elif self.direction == "B":
            if self.select_direction:
                self.get_direction = random.randint(0, 1)
                self.select_direction = False
            if self.get_direction == 0:
                self.rect.centery -= self.speed
                self.direction = "up"
            elif self.get_direction == 1:
                self.rect.centerx -= self.speed
                self.direction = "left"

        elif self.direction == "C":
            if self.select_direction:
                self.get_direction = random.randint(0, 1)
                self.select_direction = False
            if self.get_direction == 0:
                self.rect.centery -= self.speed
                self.direction = "up"
            elif self.get_direction == 1:
                self.rect.centery += self.speed
                self.direction = "down"

        elif self.direction == "D":
            if self.select_direction:
                self.get_direction = random.randint(0, 1)
                self.select_direction = False
            if self.get_direction == 0:
                self.rect.centerx += self.speed
                self.direction = "right"
            elif self.get_direction == 1:
                self.rect.centerx -= self.speed
                self.direction = "left"

        elif self.direction == "E":
            if self.select_direction:
                self.get_direction = random.randint(0, 1)
                self.select_direction = False
            if self.get_direction == 0:
                self.rect.centerx += self.speed
                self.direction = "right"
            elif self.get_direction == 1:
                self.rect.centery += self.speed
                self.direction = "down"

        elif self.direction == "F":
            if self.select_direction:
                self.get_direction = random.randint(0, 1)
                self.select_direction = False
            if self.get_direction == 0:
                self.rect.centerx -= self.speed
                self.direction = "left"
            elif self.get_direction == 1:
                self.rect.centery += self.speed
                self.direction = "down"

        self.travelled += self.speed
