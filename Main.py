import pygame, sys
from pygame.locals import *
from Towersprite import *
from Bulletsprite import *
from Functions import *
from Enemysprite import *
from math import *
from Map import *
from Road import *
from Player import *
from Environment_sprite import *
import time

# Define constant names for different colors.
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
GRAY = (128,128,128)

def menu():
    pygame.init()
    window = pygame.display.set_mode((1500,700))
    pygame.display.set_caption("Tower Defense")
    Menu_font = pygame.font.SysFont('Calibri', 45, True, False)
    Menu_text = Menu_font.render("Menu", True, BLACK)
    param_dict = Initialize() # Initializing constant names, lists, etc. that are needed in the game.
    font = pygame.font.SysFont('Calibri', 18, True, False)
    start = font.render("Start", True, BLACK)
    ExitFlag = 0 # ExitFlag is a variable that tells when we can call the function main.
    clock = pygame.time.Clock()
    Draw_static_1(window, param_dict) # Function "Draw_static_1" draws the stationary objects in the menu-screen of the game.
    while True:
        pos = pygame.mouse.get_pos()
        xpos = pos[0]
        ypos = pos[1]
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 780 and xpos < 900 and ypos > 600 and ypos < 670: # If the user clicks on the EXIT-button shown on the screen, we quit pygame and exit the program.
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 380 and xpos < 695 and ypos > 595 and ypos < 670: # If the user clicks on the INSTRUCTIONS-button shown on the screen, we call a function guide.
                guide(window)
                Draw_static_1(window, param_dict)

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 70 and xpos < 500 and ypos > 30 and ypos < 250: # User clicks on the map on the top left corner to start playing the game with that map.
                field = Map(1) # We initialize an object of the class Map. The parameter 1 is used to specify what sort of a map is to be created.
                file = "1" # This is the file that includes information of all the enemies in this map (field).
                environment_list = pygame.sprite.Group() # Environment_list will include all the environment textures that are shown in the game field.
                pieces_list = pygame.sprite.Group() # Pieces_list will include all the brown rectangles that form the path that the enemies will be travelling.
                # Here we add all the parts of the path of the enemies to pieces_list.
                pieces_list.add(Piece(0, 333, 219, 30))
                pieces_list.add(Piece(189, 81, 30, 282))
                pieces_list.add(Piece(189, 81, 324, 30))
                pieces_list.add(Piece(483, 81, 30, 534))
                pieces_list.add(Piece(483, 585, 432, 30))
                pieces_list.add(Piece(885, 483, 30, 132))
                pieces_list.add(Piece(783, 483, 132, 30))
                pieces_list.add(Piece(783, 135, 30, 378))
                pieces_list.add(Piece(783, 135, 234, 30))
                pieces_list.add(Piece(987, 0, 30, 165))

                player = Player(0,400,20)
                # Here we add environment textures to a list called "environment_list".
                environment_list.add(Environment(param_dict["tree"], 10, 550))
                environment_list.add(Environment(param_dict["tree"], 250, 500))
                environment_list.add(Environment(param_dict["tree"], 990, 300))
                environment_list.add(Environment(param_dict["tree_2"], 1090, 585))
                environment_list.add(Environment(param_dict["lake"], 270, 230))
                environment_list.add(Environment(param_dict["tree_2"], 600, 200))
                environment_list.add(Environment(param_dict["tree"], 600, 400))
                ExitFlag = 1
                break

            # User clicks on the map on the top right corner to start palying the game with that map.
            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1000 and xpos < 1430 and ypos > 30 and ypos < 250:
                field = Map(2)
                file = "2"
                environment_list = pygame.sprite.Group()
                pieces_list = pygame.sprite.Group()
                pieces_list.add(Piece(0, 85, 215, 30))
                pieces_list.add(Piece(185, 85, 30, 230))
                pieces_list.add(Piece(185, 285, 330, 30))
                pieces_list.add(Piece(485, 285, 30, 280))
                pieces_list.add(Piece(385, 535, 130, 30))
                pieces_list.add(Piece(385, 535, 30, 130))
                pieces_list.add(Piece(385, 635, 630, 30))
                pieces_list.add(Piece(985, 485, 30, 180))
                pieces_list.add(Piece(835, 485, 180, 30))
                pieces_list.add(Piece(835, 385, 30, 130))
                pieces_list.add(Piece(835, 385, 180, 30))
                pieces_list.add(Piece(985, 235, 30, 180))
                pieces_list.add(Piece(985, 235, 130, 30))
                pieces_list.add(Piece(1085, 85, 30, 180))
                pieces_list.add(Piece(885, 85, 230, 30))
                pieces_list.add(Piece(885, 0, 30, 115))

                player = Player(0,400,20)

                environment_list.add(Environment(param_dict["lake"], 535, 15))
                environment_list.add(Environment(param_dict["tree"], 10, 580))
                environment_list.add(Environment(param_dict["tree_2"], 40, 400))
                environment_list.add(Environment(param_dict["tree"], 700, 140))
                environment_list.add(Environment(param_dict["tree"], 650, 340))
                environment_list.add(Environment(param_dict["tree_2"], 400, 50))
                environment_list.add(Environment(param_dict["lake"], 190, 380))
                ExitFlag = 1
                break

            # User clicks on the map on the lower left corner to start playing the game with that map.
            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 70 and xpos < 500 and ypos > 300 and ypos < 520:
                field = Map(3)
                file = "3"
                environment_list = pygame.sprite.Group()
                pieces_list = pygame.sprite.Group()
                pieces_list.add(Piece(535, 585, 30, 115))
                pieces_list.add(Piece(285, 585, 530, 30))
                pieces_list.add(Piece(785, 435, 30, 180))
                pieces_list.add(Piece(285, 435, 30, 180))
                pieces_list.add(Piece(285, 435, 530, 30))
                pieces_list.add(Piece(785, 485, 230, 30))
                pieces_list.add(Piece(985, 255, 30, 260))
                pieces_list.add(Piece(535, 255, 480, 30))
                pieces_list.add(Piece(535, 255, 30, 210))
                pieces_list.add(Piece(0, 255, 565, 30))
                pieces_list.add(Piece(185, 85, 30, 200))
                pieces_list.add(Piece(185, 85, 80, 30))
                pieces_list.add(Piece(235, 0, 30, 115))
                pieces_list.add(Piece(85, 255, 30, 260))
                pieces_list.add(Piece(0, 485, 115, 30))

                player = Player(0,600,20)

                environment_list.add(Environment(param_dict["lake"], 1000, 20))
                environment_list.add(Environment(param_dict["tree_2"], 850, 20))
                environment_list.add(Environment(param_dict["tree"], 650, 50))
                environment_list.add(Environment(param_dict["lake"], 400, 50))
                environment_list.add(Environment(param_dict["tree"], 20, 570))
                environment_list.add(Environment(param_dict["tree_2"], 1100, 570))
                environment_list.add(Environment(param_dict["tree"], 50, 90))
                environment_list.add(Environment(param_dict["tree_2"], 170, 370))
                ExitFlag = 1
                break

            # User clicks on the map on the lower right corner to start playing the game with that map.
            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1000 and xpos < 1430 and ypos > 300 and ypos < 520:
                field = Map(4)
                file = "4"
                environment_list = pygame.sprite.Group()
                pieces_list = pygame.sprite.Group()
                pieces_list.add(Piece(585, 585, 30, 115))
                pieces_list.add(Piece(285, 585, 630, 30))
                pieces_list.add(Piece(885, 385, 30, 230))
                pieces_list.add(Piece(285, 385, 30, 230))
                pieces_list.add(Piece(685, 385, 430, 30))
                pieces_list.add(Piece(1085, 0, 30, 415))
                pieces_list.add(Piece(685, 215, 30, 200))
                pieces_list.add(Piece(485, 215, 230, 30))
                pieces_list.add(Piece(485, 215, 30, 200))
                pieces_list.add(Piece(85, 385, 430, 30))
                pieces_list.add(Piece(85, 0, 30, 415))
                pieces_list.add(Piece(0, 185, 115, 30))
                pieces_list.add(Piece(585, 105, 30, 140))
                pieces_list.add(Piece(385, 105, 430, 30))
                pieces_list.add(Piece(385, 0, 30, 135))
                pieces_list.add(Piece(785, 0, 30, 135))

                player = Player(0,600,20)

                environment_list.add(Environment(param_dict["tree"], 50, 530))
                environment_list.add(Environment(param_dict["tree"], 1050, 530))
                environment_list.add(Environment(param_dict["lake"], 210, 200))
                environment_list.add(Environment(param_dict["tree_2"], 930, 210))
                environment_list.add(Environment(param_dict["tree"], 800, 210))
                environment_list.add(Environment(param_dict["tree_2"], 210, 70))
                environment_list.add(Environment(param_dict["tree"], 570, 430))
                ExitFlag = 1
                break

        if ExitFlag != 0:
            ExitFlag = 0
            main(pieces_list, player, field, environment_list, file, window, param_dict, start, Menu_text)
            Draw_static_1(window, param_dict)

        pygame.display.update()
        clock.tick(60)

def main(pieces_list, player, field, environment_list, file, window, param_dict, start, Menu_text):
    clock = pygame.time.Clock()
    database = "Map1.db"
    round_stats = [] # round_stats is a list that contains the information of all enemies of a certain round during that round.
    i = -1 # This is a variable used for indexing the round_stats-list.
    delta = 0 # This defines how frequently new enemies are created to the game field.
    jumpLines = 0 # Explained in the function "read_file".
    StartRoundFlag = 1 # This variable ensures that the player can not start a new round before all the enemies in the previous round are eliminated.
    RoundDelta = 0 # StartRoundFlag alone cannot ensure that the player can not start a new round before all enemies are destroyed. This is because enemies are created every 0.5 seconds so it may seem to the program that all enemies are destroyed between the creation of two enemies. Variable RoundDelta ensures that the field must be empty of enemies for at least 0.6 seconds before the player can start a new round.
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            xpos = pos[0]
            ypos = pos[1]
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1420 and ypos < 80: # Select machine gun tower.
                (tower, round_stats, delta, i) = Set_machine_gun(param_dict, window, pieces_list, round_stats, delta, i, player, start, field, jumpLines, environment_list)
                if tower != None: # Tower successfully placed to the game field.
                    param_dict["tower_list"].add(tower) # We add the created tower to a list that includes all the towers in the game field.

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1340 and xpos < 1420 and ypos < 80: # Select shotgun tower.
                (tower, round_stats, delta, i) = Set_shotgun(param_dict, window, pieces_list, round_stats, delta, i, player, start, field, jumpLines, environment_list)
                if (tower != None):
                    param_dict["tower_list"].add(tower)

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1260 and xpos < 1340 and ypos < 80: # Select assistant tower.
                (tower, round_stats, delta, i) = Set_assistant(param_dict, window, pieces_list, round_stats, delta, i, player, start, field, jumpLines, environment_list)
                if (tower != None):
                    param_dict["tower_list"].add(tower)

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1180 and xpos < 1260 and ypos < 80: # Select pistol tower.
                (tower, round_stats, delta, i) = Set_pistol(param_dict, window, pieces_list, round_stats, delta, i, player, start, field, jumpLines, environment_list)
                if (tower != None):
                    param_dict["tower_list"].add(tower)

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1180 and xpos < 1260 and ypos < 192 and ypos > 112: # Select mine.
                (tower, round_stats, delta, i) = Set_mine(param_dict, window, pieces_list, round_stats, delta, i, player, start, field, jumpLines, environment_list)
                if (tower != None):
                    param_dict["contact_bomb_list"].add(tower)

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1260 and xpos < 1340 and ypos < 192 and ypos > 112: # Select smart bomb.
                (tower, round_stats, delta, i) = Set_smart_bomb(param_dict, window, pieces_list, round_stats, delta, i, player, start, field, jumpLines, environment_list)
                if (tower != None):
                    param_dict["range_bomb_list"].add(tower)

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1340 and xpos < 1420 and ypos < 192 and ypos > 112: # Select homing missile.
                (tower, round_stats, delta, i) = Set_homing_missile(param_dict, window, pieces_list, round_stats, delta, i, player, start, field, jumpLines, environment_list)
                if tower != None:
                    param_dict["tower_list"].add(tower)

            elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE: # Pause the game.
                pygame.draw.rect(window, WHITE, (1180, 602, 1500, 700), 0)
                window.blit(Menu_text, (1280, 630)) # Draw a text "MENU" in place of "START ROUND".
                diff = float(time.monotonic()) - delta # Diff is a variable that contains the difference of current time and the time when the previous enemy was created.
                while True:
                    n = 0
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:  # If the player presses ESC again, break out of this loop and continue playing the game.
                            n = 1
                            break
                        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 1180 and pygame.mouse.get_pos()[1] > 600: # If the player clicks on the "MENU"-button, return back to the menu-function.
                            param_dict["tower_list"].empty()
                            param_dict["bullet_list"].empty()
                            param_dict["enemy_list"].empty()
                            del param_dict["range_list"][:]
                            del param_dict["value_list"][:]
                            param_dict["dictionary"].clear()
                            param_dict["contact_bomb_list"].empty()
                            param_dict["range_bomb_list"].empty()
                            param_dict["missile_list"].empty()
                            return
                        elif event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        pygame.display.update()
                        clock.tick(60)
                    if n == 1:
                        delta = float(time.monotonic()) - diff
                        break

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1180 and ypos > 600 and StartRoundFlag == 1: # Player clicks on the "START ROUND"-button.
                round_stats = read(field, file, jumpLines, player, window, database)
                if round_stats[0] == "RET":
                    param_dict["tower_list"].empty()
                    param_dict["bullet_list"].empty()
                    param_dict["enemy_list"].empty()
                    del param_dict["range_list"][:]
                    del param_dict["value_list"][:]
                    param_dict["dictionary"].clear()
                    param_dict["contact_bomb_list"].empty()
                    param_dict["range_bomb_list"].empty()
                    param_dict["missile_list"].empty()
                    return
                jumpLines += 1 # Variable jumpLines tells the program which line to read in the file that contains information about the enemies in a certain field.
                delta = float(time.monotonic())
                i = 0
                StartRoundFlag = 0
                RoundDelta = float(time.monotonic())

            for tower in param_dict["tower_list"]: # Loop through all enemies.
                # The user clicks on some tower on the field to do some operations on it.
                if event.type == pygame.MOUSEBUTTONDOWN and xpos > (tower.rect.centerx-10) and xpos < (tower.rect.centerx+10) and ypos > (tower.rect.centery-10) and ypos < (tower.rect.centery+10):
                    (tower, round_stats, delta, i) = Draw_2(param_dict, window, pieces_list, round_stats, delta, i, tower, player, start, field, jumpLines, environment_list)

            for tower in param_dict["contact_bomb_list"]: # Loop through all the mines that are in the game field.
                if event.type == pygame.MOUSEBUTTONDOWN and xpos > (tower.rect.centerx-10) and xpos < (tower.rect.centerx+10) and ypos > (tower.rect.centery-10) and ypos < (tower.rect.centery+10):
                    (tower, round_stats, delta, i) = Draw_2(param_dict, window, pieces_list, round_stats, delta, i, tower, player, start, field, jumpLines, environment_list)

            for tower in param_dict["range_bomb_list"]: # Loop through all the smart bombs that are in the game field.
                if event.type == pygame.MOUSEBUTTONDOWN and xpos > (tower.rect.centerx-10) and xpos < (tower.rect.centerx+10) and ypos > (tower.rect.centery-10) and ypos < (tower.rect.centery+10):
                    (tower, round_stats, delta, i) = Draw_2(param_dict, window, pieces_list, round_stats, delta, i, tower, player, start, field, jumpLines, environment_list)

        if float(time.monotonic()) - delta > 0.5 and i < len(round_stats) and i != -1: # Add an enemy in the round_stats-list to a pygame.sprite.group()-type list.
            param_dict["enemy_list"].add(round_stats[i])
            delta = float(time.monotonic())
            if len(round_stats) - i == 1: # If all enemies in the round_stats-list have already been added.
                del round_stats[:] # Remove all content in round_stats-list.
                i = -1
            else:
                i = i + 1
        Draw_static(window, param_dict, pieces_list, player, environment_list) # Draw all the stationary ojects in the game screen.

        param_dict["tower_list"].draw(window) # Draw all towers to the game field.
        param_dict["contact_bomb_list"].draw(window) # Draw all mines to the game field.
        param_dict["range_bomb_list"].draw(window) # Draw all smart bombs to the game field.
        for enemy in param_dict["enemy_list"]: # Loop through all enemies in the game field.
            if enemy.direction == "up" or enemy.direction == "down":
                window.blit((param_dict["font"].render(str(enemy.health), True, BLACK)), (enemy.rect.centerx + 16, enemy.rect.centery - 7)) # Draw health of the enemy next to the enemy.
            elif enemy.direction == "left" or enemy.direction == "right":
                window.blit((param_dict["font"].render(str(enemy.health), True, BLACK)), (enemy.rect.x, enemy.rect.centery - 28))
            if enemy.health <= 0:
                enemy.kill()
                player.Money += enemy.price
            if enemy.rect.centerx < 0 or enemy.rect.centerx > 1500 or enemy.rect.centery < 0 or enemy.rect.centery > 700: # If an enemy goes outside the game field, remove the enemy and reduce player lives by one.
                enemy.kill()
                player.Lives -= 1
                if player.Lives <= 0:
                    game_over(window)
                    param_dict["tower_list"].empty()
                    param_dict["bullet_list"].empty()
                    param_dict["enemy_list"].empty()
                    del param_dict["range_list"][:]
                    del param_dict["value_list"][:]
                    param_dict["dictionary"].clear()
                    param_dict["contact_bomb_list"].empty()
                    param_dict["range_bomb_list"].empty()
                    param_dict["missile_list"].empty()
                    return

        for tower in param_dict["contact_bomb_list"]: # Loop through all the mines in the field.
            if xpos > (tower.rect.centerx-10) and xpos < (tower.rect.centerx+10) and ypos > (tower.rect.centery-10) and ypos < (tower.rect.centery+10): # If the player moves a cursor on top of a mine, draw a blue circle around it.
                pygame.draw.circle(window, BLUE, (tower.rect.centerx, tower.rect.centery), 100, 1)
            for enemy in param_dict["enemy_list"]: # Loop through all enemies in the field.
                if enemy.health <= 0:
                    enemy.kill()
                    player.Money += enemy.price
                if pygame.sprite.collide_rect(tower, enemy): # If an enemy and a mine collide, reduce the health of an enemy and remove the mine.
                    enemy.health -= tower.damage
                    tower.kill()

        for tower in param_dict["range_bomb_list"]: # Loop through all the smart bombs in the field.
            # If the player moves a cursor on top of a bomb, draw a blue circle around it.
            if xpos > (tower.rect.centerx-10) and xpos < (tower.rect.centerx+10) and ypos > (tower.rect.centery-10) and ypos < (tower.rect.centery+10):
                pygame.draw.circle(window, BLUE, (tower.rect.centerx, tower.rect.centery), 100, 1)
            for enemy in param_dict["enemy_list"]: # Loop through all the enemies.
                enemy.dist = sqrt((enemy.rect.centerx - tower.rect.centerx)**2 + (enemy.rect.centery - tower.rect.centery)**2) # Calculate the distance of an enemy from a smart bomb.
                if enemy.health <= 0:
                    enemy.kill()
                    player.Money += enemy.price
                # If the distance of an enemy from the tower is at most 100, we add an enemy to a list that contains all the enemies that are at most a distance of 100 from the smart bomb. The condition "tower.nuber == 0" ensurest that this is not done, if the bomb has already exploded but it has not been removed yet
                if enemy.dist <= 100 and tower.number == 0:
                    tower.elist.append(enemy)
            if len(tower.elist) >= 5:
                if tower.number == 0:
                    tower.t = float(time.monotonic()) # tower.t is a counter used for defining how long a red circle is shown around the bomb when the bomb explodes.
                    for enemy in tower.elist: # Loop through all the enemies within the range of a bomb and reduce health by 100.
                        enemy.health -= 100
                tower.number = 1
                tower.elist = [0,1,2,3,4]
                if float(time.monotonic()) - tower.t < 1.0:
                    pygame.draw.circle(window, RED, (tower.rect.centerx, tower.rect.centery), 100, 0)
                else:
                    tower.kill()
            if tower.number == 0:
                del tower.elist[:]

        for bullet in param_dict["missile_list"]: # Loop through all the missiles in the field.
            # Set the target of the missile to be the current coordinates of the enemy that was the target when the missile was created.
            bullet.target = [bullet.target_enemy.rect.centerx, bullet.target_enemy.rect.centery]

        for tower in param_dict["tower_list"]: # Loop through all the basic towers in the field.
            # Draw the pipe of the tower to point straight up. The variable "tower.PipeUp" ensurest that the pipe is drawn to point up only when it has not yet been set to point towards some enemy.
            if tower.PipeUp == 0:
                tower.x0 = tower.rect.centerx
                tower.y0 = tower.rect.centery - 12
                tower.PipeUp = 1
            pygame.draw.line(window, BLACK, (tower.rect.centerx, tower.rect.centery), (tower.x0, tower.y0), 1)
            # If the player sets the cursor on top of some tower, draw a blue circle around the tower that describes the range of the tower.
            if (xpos > (tower.rect.centerx-10) and xpos < (tower.rect.centerx+10) and ypos > (tower.rect.centery-10) and ypos < (tower.rect.centery+10)):
                pygame.draw.circle(window, BLUE, (tower.rect.centerx, tower.rect.centery), tower.range, 1)
            for enemy in param_dict["enemy_list"]: # Loop through all enemies in the field
                if (enemy.health <= 0):
                    enemy.kill()
                    player.Money += enemy.price
                enemy.dist = sqrt((enemy.rect.centerx - tower.rect.centerx)**2 + (enemy.rect.centery - tower.rect.centery)**2) # Calculate the of an enemy from a tower.
                if enemy.dist <= tower.range: # If an enemy is within the range of a tower.
                    param_dict["range_list"].append(enemy) # Add the enemy to a list that includes all enemies that are within the range of a tower.
                    param_dict["dictionary"][enemy.value] = enemy # Add a new key and a value corresponding to that key to a dictionary. The key is a "value"-variable of an enemy and the value is the enemy. The "enemy.value" is a variable that depends linearly on the length the enemy has travelled in the field.
                    param_dict["value_list"].append(enemy.value) # Add the enemy.value-variable to a distinct list.
                for bullet in param_dict["bullet_list"]: # Loop through all the bullets in the field.
                    if pygame.sprite.collide_rect(bullet, enemy): # If enemy and bullet collide.
                        if bullet.type_2 != enemy.resistant: # "bullet.type_2" is a variable (integer from 1-5) that tells to whcih tower the enemy is immune.
                            enemy.health -= bullet.damage # Reduce the health of an enemy.
                            if bullet.poison == 1 and enemy.poison == 0: # If the bullet is poisonous and the enemy is not already poisoned, poison the enemy.
                                enemy.poison = 1
                                enemy.poisonTime = time.monotonic() # "enemy.t" is a variable that defines how quickly the poison affects the enemy.
                            if bullet.type == 2: # If a bullet is shot by an assistant-tower.
                                if enemy.speed == 2: # If the enemy is moving quickly we reduce the speed of the enemy.
                                    enemy.speed = 1
                                if enemy.resistant != 5: # If an enemy is immune to some tower, remove the immunity.
                                    enemy.resistant = 5
                                enemy.image = black_monster # Turn the enemy to black.
                        bullet.kill() # Remove the bullet.
                for bullet in param_dict["missile_list"]: # Loop through all the missiles in the field.
                    # If a missile and an enemy collide and the enemy is not immune to a missile, reduce the health of an enemy.
                    if pygame.sprite.collide_rect(bullet, enemy):
                        if bullet.type_2 != enemy.resistant:
                            enemy.health -= bullet.damage
                            if bullet.poison == 1 and enemy.poison == 0:
                                enemy.poison = 1
                                enemy.poisonTime = time.monotonic()
                        bullet.kill()
                        
            param_dict["value_list"].sort() # Sort the list that contains value-parameters of the enemies from smallest to largest.
            param_dict["value_list"].reverse()
            if float(time.monotonic()) - float(tower.beginning) >= tower.interval and (param_dict["value_list"]): # Check if enough time has passed from the previous shot so that we can shoot again.
                target = [param_dict["dictionary"][param_dict["value_list"][0]].rect.centerx, param_dict["dictionary"][param_dict["value_list"][0]].rect.centery] # Set the target to be the enemy that has travelled the longest distance.
                startpoint = [tower.rect.centerx, tower.rect.centery] # The startpoint of the bullet is the coordinates of the tower that shoots the bullet.
                # tower.x0 and tower.y0 are the endpoint coordinates of the pipe of a tower.
                tower.x0 = startpoint[0] + 12*(target[0]-startpoint[0]) / param_dict["dictionary"][param_dict["value_list"][0]].dist
                tower.y0 = startpoint[1] + 12*(target[1]-startpoint[1]) / param_dict["dictionary"][param_dict["value_list"][0]].dist
                # Draw the pipe of the tower to point towards the enemy that the tower is shooting.
                pygame.draw.line(window, BLACK, (startpoint[0], startpoint[1]), (round(tower.x0), round(tower.y0)), 1)
                # Set some properties for the bullet. These properties are dependent on the tower that shoots the bullet.
                damage = tower.damage
                poison = tower.poison
                Type = tower.type
                Type_2 = tower.type_2
                bullet = Bullet(target, startpoint, damage, poison, Type, Type_2, param_dict["dictionary"][param_dict["value_list"][0]]) # Create an object of class Bullet that represents a moving bullet.
                # Add the created bullet to one of two lists depending on whether the bullet is homing or not.
                if tower.homing == 0: # The bullet is not homing.
                    param_dict["bullet_list"].add(bullet)
                elif tower.homing == 1: # The bullet is homing.
                    param_dict["missile_list"].add(bullet)
                tower.beginning = time.monotonic() # This is the moment when a tower shoots a bullet.
            del param_dict["value_list"][:]
            del param_dict["range_list"][:]
            param_dict["dictionary"].clear()
        if (len(param_dict["enemy_list"]) != 0): # If the list containing all the enemies is empty.
            RoundDelta = float(time.monotonic())
        if (float(time.monotonic()) - RoundDelta > 0.6): # If it has passed at least 0.6 seconds since the list containing the enemies was cleared, we enable the possibility to press the "start round"-button.
            StartRoundFlag = 1

        # Display a text "start" in the beginning of the path that the enemies travel so that the player knows where they start coming. This text is removed when the player clicks on the "Start round"-button for the first time.
        if (jumpLines == 0 and field.number == 1):
            window.blit(start, (5, 315))
        elif (jumpLines == 0 and field.number == 2):
            window.blit(start, (5, 67))
        elif (jumpLines == 0 and field.number == 3):
            window.blit(start, (570, 670))
        elif (jumpLines == 0 and field.number == 4):
            window.blit(start, (620, 670))
        # Update the lists that contain the enemies and bullets and draw these on the game field.
        param_dict["bullet_list"].update()
        param_dict["enemy_list"].update()
        param_dict["missile_list"].update()
        param_dict["bullet_list"].draw(window)
        param_dict["enemy_list"].draw(window)
        param_dict["missile_list"].draw(window)
        del param_dict["value_list"][:]
        del param_dict["range_list"][:]
        param_dict["dictionary"].clear()
        pygame.display.update()
        clock.tick(60)
menu()
