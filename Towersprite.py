import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Machine_gun_tower(Tower):
    def __init__(self, picture, beginning):
        super().__init__()
        # Picture is the image that represents a tower when it has been set to the game field.
        self.image = picture
        self.beginning = beginning  # Beginning is the moment when the tower is set to the field.
        self.rect = self.image.get_rect()
        self.range = 100  # The range of a tower.
        self.interval = 0.22  # The time in seconds that a tower has to wait between two shots.
        self.damage = 15  # The damage a tower makes to an enemy.
        self.price = 350  # The price of a tower.
        # This defines whether the bullets that this tower shoots are poisonous or not.
        # If self.poison = 0, bullets are not poisonous and if self.poison = 1,
        # bullets are poisonous.
        self.poison = 0
        self.is_assistant = False
        self.bullet_type = 1  # Defines wheter an enemy is immune to this type of tower.
        # This variable is False if the range of this tower has not yet been updated.
        # When range is updated, this is set to True.
        self.range_state = False
        # This variable is False if the shooting rate of this tower has not yet been updated.
        # When shooting rate is updated, this is set to True.
        self.rate_state = False
        # This variable is False if the damage of this tower has not yet been updated.
        # When damage is updated, this is set to True.
        self.damage_state = False
        # This variable is False if this tower has no poisoning property.
        # When poisoning property is added, this is set to True.
        self.poison_state = False
        self.pipe_up = True  # This controls when the pipe of the tower is drawn to point upwards.
        self.x0 = 0  # X-coordinate of the endpoint of the pipe of the tower.
        self.y0 = 0  # Y-coordinate of the endpoint of the pipe of the tower.
        self.homing = 0  # Defines whether the tower shoots homing bullets or not.


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
        self.is_assistant = False
        self.bullet_type = 6
        self.range_state = False
        self.rate_state = False
        self.damage_state = False
        self.poison_state = False
        self.pipe_up = True
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
        self.is_assistant = False
        self.bullet_type = 4
        self.range_state = False
        self.rate_state = False
        self.damage_state = False
        self.poison_state = False
        self.pipe_up = True
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
        self.is_assistant = True
        self.bullet_type = 2
        self.range_state = False
        self.rate_state = False
        self.damage_state = False
        self.poison_state = False
        self.pipe_up = True
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
        self.is_assistant = False
        self.bullet_type = 3
        self.range_state = False
        self.rate_state = False
        self.damage_state = False
        self.poison_state = False
        self.pipe_up = True
        self.x0 = 0
        self.y0 = 0
        self.homing = 0


class Mine(Tower):
    def __init__(self, picture):
        super().__init__()
        self.image = picture
        self.rect = self.image.get_rect()
        self.damage = 50
        self.price = 150
        self.range = 100


class Smart_bomb(Tower):
    def __init__(self, picture):
        super().__init__()
        self.image = picture
        self.rect = self.image.get_rect()
        self.damage = 80
        self.price = 300
        self.elist = []  # A list that contains the enemies within the range of a bomb.
        self.t = 0  # How long a red circle is drawn around a bomb when it explodes.
        self.number = 0
        self.range = 100
