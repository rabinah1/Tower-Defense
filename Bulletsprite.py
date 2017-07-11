import pygame
from pygame.locals import *
from math import *

class Bullet(pygame.sprite.Sprite): # Create a class for a bullet
    def __init__(self, target, startpoint, damage, poison, Type, Type_2, target_enemy):
        super().__init__()
        self.image = pygame.Surface((4,4)) # Define a 4x4-pixel square as the image of a bullet.
        self.image.fill((0,0,0)) # Paint the bullet balck.
        self.rect = self.image.get_rect()
        self.target = target # The target toward witch the bullet is heading.
        self.startpoint = startpoint # The startpoint of the bullet, that is, the coordinates of the tower that shoots the bullet.
        self.xdir = 0.0 # The precise value for how much the bullet should be moved in x-direction within one loop iteration.
        self.ydir = 0.0 # The precise value for how much the bullet shoudl be moved in y-direction within one loop iteration.
        self.rect.centerx = self.startpoint[0] # X-coordinate of the bullet in the beginning = X-coordinate of the startpoint in the beginning.
        self.rect.centery = self.startpoint[1] # Y-coordinate of the bullet in the beginning = Y-coordinate of the startpoint in the beginning.
        self.slope = 0.0 # The slope of the line between the startpoint of the bullet and the target of the bullet.
        self.prev_slope = 1.0 # This variable holds the "previous slope" (the slope in the previous iteration in the loop).
        self.n = 1 # A counter that defines whether we round the x- and y-coordinate of the bullet up or down.
        self.dist = 0 # The distance between current coordinates of the bullet and the coordinates of the target of the bullet.
        self.damage = damage # Defines how much the bullet causes damage to the enemy.
        self.poison = poison # Defines whether the bullet is poisonous.
        self.type = Type # Defines whether the tower that shoots the bullet is of type assistant of some other.
        self.type_2 = Type_2 # Defines what enemy is immune to this bullet.
        self.x_diff = 0.0 # The difference between the x-coordinates of the first and second position of the bullet.
        self.y_diff = 0.0 # The difference between the y-coordinates of the first and second position of the bullet.
        self.count_y = 0 # A variable that controls that the difference in the y-coordinates is calculated from the first and second points.
        self.count_x = 0 # A variable that controls that the difference in the x-coordinates is calculated from the first and second points.
        self.dist_count = 0 # A variable that controls when to stop calculating a distance to the target.
        self.target_enemy = target_enemy # The enemy toward which a homing missile is propagating.
    
    # The algorithm that controls the propagation of a bullet.
    def update(self):
        if self.dist_count == 0:
            self.dist = sqrt((self.target[0]-self.rect.centerx)**2 + (self.target[1]-self.rect.centery)**2) # Calculate the distance between the bullet and the taget of the bullet.
        # If the bullet has not yet reached its target neither in x- or y-directions and the distance between the bullet and target is over 7.50 pixels.
        if (self.target[0] - self.rect.centerx) != 0 and (self.target[1] - self.rect.centery) != 0 and self.dist > 7.50:
            if self.target[0] - self.startpoint[0] != 0:
                self.slope = (self.target[1] - self.startpoint[1]) / (self.target[0] - self.startpoint[0]) # Define the slop.
                self.prev_slope = self.slope
            else:
                self.slope = self.prev_slope
            # If the distance between the bullet and the target is smaller in x-direction than in y-direction, we first update y-coordinate of the bullet by 10 pixels. After this we update x-coordinate by amount defined by the starting point and the line between the startpoint and the target. All necessary expression can be derivated from the equation y-y0 = k(x-x0) where (x0, y0) are the coordinates of the target of the bullet.
            if abs(self.target[0] - self.rect.centerx) < abs(self.target[1] - self.rect.centery):
                self.rect.centery += 10*((self.target[1] - self.rect.centery) / ((abs(self.target[1] - self.rect.centery))))
                if self.count_y == 0:
                    self.y_diff = round(self.rect.centery - self.startpoint[1])
                    self.count_y = 1
                self.xdir = (self.rect.centery - self.target[1] + self.slope * self.target[0]) / self.slope
                # Round the exact value of the movement in the x-direction every other time up and every other time down to the nearest integer so that the direction of the bullet does not change.
                if self.n % 2 == 0:
                    self.rect.centerx = floor(self.xdir)
                    if self.count_x == 0:
                        self.x_diff = round(self.rect.centerx - self.startpoint[0])
                        self.count_x = 1
                    self.n += 1
                else:
                    self.rect.centerx = ceil(self.xdir)
                    if self.count_x == 0:
                        self.x_diff = round(self.rect.centerx - self.startpoint[0])
                        self.count_x = 1
                    self.n += 1
            # If the distance between the bullet and the target is bigger in x-direction than in y-direction, we first update x-coordinate of the bullet by 10 pixels. After this we update y-coordinate by an amount defined by the startin point and the line between tha startpoing and the target.
            elif abs(self.target[0] - self.rect.centerx) > abs(self.target[1] - self.rect.centery):
                self.rect.centerx += 10*((self.target[0] - self.rect.centerx) / ((abs(self.target[0] - self.rect.centerx))))
                if self.count_x == 0:
                    self.x_diff = round(self.rect.centerx - self.startpoint[0])
                    self.count_x = 1
                self.ydir = self.slope * (self.rect.centerx - self.target[0]) + self.target[1]
                # Round the exact value of the moevemtn in the y-direction every other time up and every ohter time down to the nearest integer so that the direction of the bullet does not change.
                if self.n % 2 == 0:
                    self.rect.centery = floor(self.ydir)
                    if self.count_y == 0:
                        self.y_diff = round(self.rect.centery - self.startpoint[1])
                        self.count_y = 1
                    self.n += 1
                else:
                    self.rect.centery = ceil(self.ydir)
                    if self.count_y == 0:
                        self.y_diff = round(self.rect.centery - self.startpoint[1])
                        self.count_y = 1
                    self.n += 1
            # If the distance between the bullet and the target in the x-direction equals the distance in y-direction, we update both coordinates by 10 pixels.
            elif abs(self.target[0] - self.rect.centerx) == abs(self.target[1] - self.rect.centery):
                self.rect.centerx += 10*((self.target[0] - self.rect.centerx) / ((abs(self.target[0] - self.rect.centerx))))
                self.rect.centery += 10*((self.target[1] - self.rect.centery) / ((abs(self.target[1] - self.rect.centery))))
                if self.count_x == 0:
                    self.x_diff = round(self.rect.centerx - self.startpoint[0])
                    self.count_x = 1
                if self.count_y == 0:
                    self.y_diff = round(self.rect.centery - self.startpoint[1])
                    self.count_y = 1
        
        # If the distance between the bullet and the target in x-direction is zero, we only update y-coordinate by 10 pixels.
        elif (self.target[0] - self.rect.centerx) == 0 and (self.target[1] - self.rect.centery) != 0 and self.dist > 7.50:
            self.rect.centery += 10*((self.target[1] - self.rect.centery) / ((abs(self.target[1] - self.rect.centery))))
            if self.count_y == 0:
                self.y_diff = round(self.rect.centery - self.startpoint[1])
                self.count_y = 1
         
        # If the distance between the bullet and the target in y-direction is zero, we only update x-coordinate by 10 pixels.  
        elif (self.target[0] - self.rect.centerx) != 0 and (self.target[1] - self.rect.centery) == 0 and self.dist > 7.50:
            self.rect.centerx += 10*((self.target[0] - self.rect.centerx) / ((abs(self.target[0] - self.rect.centerx))))
            if self.count_x == 0:
                self.x_diff = round(self.rect.centerx - self.startpoint[0])
                self.count_x = 1
        
        # If the distance between the bullet and the target is less than 7.50 pixels, we destroy the bullet.
        elif self.dist <= 7.50:
            self.dist = 0.0
            self.dist_count = 1
            self.n = 1
            self.rect.centerx += self.x_diff
            self.rect.centery += self.y_diff
            if self.rect.centerx > 1178 or self.rect.centerx < 0 or self.rect.centery > 700 or self.rect.centery < 0:
                self.kill()
