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
    param_dict = Initialize()
    font = pygame.font.SysFont('Calibri', 18, True, False)
    start = font.render("Start", True, BLACK)
    ExitFlag = 0
    clock = pygame.time.Clock()
    Draw_static_1(window, param_dict)
    while True:
        pos = pygame.mouse.get_pos()
        xpos = pos[0]
        ypos = pos[1]
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 780 and xpos < 900 and
                  ypos > 600 and ypos < 670): # User clicks on the EXIT-button
                pygame.quit()
                sys.exit()

            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 380 and xpos < 695 and
                  ypos > 595 and ypos < 670): # User clicks on the INSTRUCTIONS-button
                guide(window)
                Draw_static_1(window, param_dict)

            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 70 and xpos < 500 and
                  ypos > 30 and ypos < 250): # User clicks on the map on the top left corner
                field = Map(1)
                file = "1"
                environment_list = pygame.sprite.Group()
                pieces_list = pygame.sprite.Group()
                # Add all the parts of the path of the enemies to pieces_list.
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
                # Add environment textures to a list called "environment_list".
                environment_list.add(Environment(param_dict["tree"], 10, 550))
                environment_list.add(Environment(param_dict["tree"], 250, 500))
                environment_list.add(Environment(param_dict["tree"], 990, 300))
                environment_list.add(Environment(param_dict["tree_2"], 1090, 585))
                environment_list.add(Environment(param_dict["lake"], 270, 230))
                environment_list.add(Environment(param_dict["tree_2"], 600, 200))
                environment_list.add(Environment(param_dict["tree"], 600, 400))
                ExitFlag = 1
                break

            # User clicks on the map on the top right corner
            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 1000 and xpos < 1430 and
                  ypos > 30 and ypos < 250):
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

            # User clicks on the map on the lower left corner
            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 70 and xpos < 500 and
                  ypos > 300 and ypos < 520):
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

            # User clicks on the map on the lower right corner
            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 1000 and xpos < 1430 and
                  ypos > 300 and ypos < 520):
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
    round_stats = [] # A list that contains the information of all enemies of a certain round
    i = -1 # A variable used for indexing the round_stats-list
    delta = 0 # How frequently new enemies are created to the game field
    jumpLines = 0 # Explained in the function "read_file"
    StartRoundFlag = 1
    RoundDelta = 0
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            xpos = pos[0]
            ypos = pos[1]
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1420 and ypos < 80: # Select machine gun tower
                (tower, round_stats, delta, i) = Set_machine_gun(param_dict, window, pieces_list,
                                                                 round_stats, delta, i, player,
                                                                 start, field, jumpLines,
                                                                 environment_list)
                if tower != None:
                    param_dict["tower_list"].add(tower)

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1340 and xpos < 1420 and ypos < 80: # Select shotgun tower
                (tower, round_stats, delta, i) = Set_shotgun(param_dict, window, pieces_list,
                                                             round_stats, delta, i, player,
                                                             start, field, jumpLines,
                                                             environment_list)
                if (tower != None):
                    param_dict["tower_list"].add(tower)

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1260 and xpos < 1340 and ypos < 80: # Select assistant tower.
                (tower, round_stats, delta, i) = Set_assistant(param_dict, window, pieces_list,
                                                               round_stats, delta, i, player,
                                                               start, field, jumpLines,
                                                               environment_list)
                if (tower != None):
                    param_dict["tower_list"].add(tower)

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1180 and xpos < 1260 and ypos < 80: # Select pistol tower.
                (tower, round_stats, delta, i) = Set_pistol(param_dict, window, pieces_list,
                                                            round_stats, delta, i, player,
                                                            start, field, jumpLines,
                                                            environment_list)
                if (tower != None):
                    param_dict["tower_list"].add(tower)

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1180 and xpos < 1260 and ypos < 192 and ypos > 112: # Select mine.
                (tower, round_stats, delta, i) = Set_mine(param_dict, window, pieces_list,
                                                          round_stats, delta, i, player,
                                                          start, field, jumpLines,
                                                          environment_list)
                if (tower != None):
                    param_dict["contact_bomb_list"].add(tower)

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1260 and xpos < 1340 and ypos < 192 and ypos > 112: # Select smart bomb.
                (tower, round_stats, delta, i) = Set_smart_bomb(param_dict, window, pieces_list,
                                                                round_stats, delta, i, player,
                                                                start, field, jumpLines,
                                                                environment_list)
                if (tower != None):
                    param_dict["range_bomb_list"].add(tower)

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1340 and xpos < 1420 and ypos < 192 and ypos > 112: # Select homing missile.
                (tower, round_stats, delta, i) = Set_homing_missile(param_dict, window, pieces_list,
                                                                    round_stats, delta, i, player,
                                                                    start, field, jumpLines,
                                                                    environment_list)
                if tower != None:
                    param_dict["tower_list"].add(tower)

            elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE: # Pause the game.
                pygame.draw.rect(window, WHITE, (1180, 602, 1500, 700), 0)
                window.blit(Menu_text, (1280, 630))
                diff = float(time.monotonic()) - delta
                while True:
                    n = 0
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                            n = 1
                            break
                        elif (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 1180 and
                              pygame.mouse.get_pos()[1] > 600): # Player clicks on the "MENU"-button
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

            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1180 and ypos > 600 and StartRoundFlag == 1: # Player clicks on the "START ROUND"-button
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
                jumpLines += 1
                delta = float(time.monotonic())
                i = 0
                StartRoundFlag = 0
                RoundDelta = float(time.monotonic())

            for tower in param_dict["tower_list"]: # Loop through all towers
                if (event.type == pygame.MOUSEBUTTONDOWN and xpos > (tower.rect.centerx-10) and
                    xpos < (tower.rect.centerx+10) and ypos > (tower.rect.centery-10) and
                    ypos < (tower.rect.centery+10)):
                    (tower, round_stats, delta, i) = Draw_2(param_dict, window, pieces_list,
                                                            round_stats, delta, i, tower, player,
                                                            start, field, jumpLines, environment_list)

            for tower in param_dict["contact_bomb_list"]: # Loop through all mines
                if (event.type == pygame.MOUSEBUTTONDOWN and xpos > (tower.rect.centerx-10) and
                    xpos < (tower.rect.centerx+10) and ypos > (tower.rect.centery-10) and
                    ypos < (tower.rect.centery+10)):
                    (tower, round_stats, delta, i) = Draw_2(param_dict, window, pieces_list,
                                                            round_stats, delta, i, tower, player,
                                                            start, field, jumpLines, environment_list)

            for tower in param_dict["range_bomb_list"]: # Loop through all smart bombs
                if (event.type == pygame.MOUSEBUTTONDOWN and xpos > (tower.rect.centerx-10) and
                    xpos < (tower.rect.centerx+10) and ypos > (tower.rect.centery-10) and
                    ypos < (tower.rect.centery+10)):
                    (tower, round_stats, delta, i) = Draw_2(param_dict, window, pieces_list,
                                                            round_stats, delta, i, tower, player,
                                                            start, field, jumpLines, environment_list)

        if float(time.monotonic()) - delta > 0.5 and i < len(round_stats) and i != -1:
            param_dict["enemy_list"].add(round_stats[i])
            delta = float(time.monotonic())
            if len(round_stats) - i == 1:
                del round_stats[:]
                i = -1
            else:
                i = i + 1
        Draw_static(window, param_dict, pieces_list, player, environment_list)

        param_dict["tower_list"].draw(window)
        param_dict["contact_bomb_list"].draw(window)
        param_dict["range_bomb_list"].draw(window)
        for enemy in param_dict["enemy_list"]:
            if enemy.direction == "up" or enemy.direction == "down":
                window.blit((param_dict["font"].render(str(enemy.health), True, BLACK)),
                            (enemy.rect.centerx + 16, enemy.rect.centery - 7))
            elif enemy.direction == "left" or enemy.direction == "right":
                window.blit((param_dict["font"].render(str(enemy.health), True, BLACK)),
                            (enemy.rect.x, enemy.rect.centery - 28))
            if enemy.health <= 0:
                enemy.kill()
                player.Money += enemy.price
            if (enemy.rect.centerx < 0 or enemy.rect.centerx > 1500 or
                enemy.rect.centery < 0 or enemy.rect.centery > 700): # Enemy goes outside the game field
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

        for tower in param_dict["contact_bomb_list"]:
            if (xpos > (tower.rect.centerx-10) and xpos < (tower.rect.centerx+10) and
                ypos > (tower.rect.centery-10) and ypos < (tower.rect.centery+10)):
                pygame.draw.circle(window, BLUE, (tower.rect.centerx, tower.rect.centery), 100, 1)
            for enemy in param_dict["enemy_list"]:
                if enemy.health <= 0:
                    enemy.kill()
                    player.Money += enemy.price
                if pygame.sprite.collide_rect(tower, enemy):
                    enemy.health -= tower.damage
                    tower.kill()

        for tower in param_dict["range_bomb_list"]:
            if (xpos > (tower.rect.centerx-10) and xpos < (tower.rect.centerx+10) and
                ypos > (tower.rect.centery-10) and ypos < (tower.rect.centery+10)):
                pygame.draw.circle(window, BLUE, (tower.rect.centerx, tower.rect.centery), 100, 1)
            for enemy in param_dict["enemy_list"]:
                enemy.dist = sqrt((enemy.rect.centerx - tower.rect.centerx)**2 +
                                  (enemy.rect.centery - tower.rect.centery)**2)
                if enemy.health <= 0:
                    enemy.kill()
                    player.Money += enemy.price
                if enemy.dist <= 100 and tower.number == 0:
                    tower.elist.append(enemy)
            if len(tower.elist) >= 5:
                if tower.number == 0:
                    tower.t = float(time.monotonic())
                    for enemy in tower.elist:
                        enemy.health -= 100
                tower.number = 1
                tower.elist = [0,1,2,3,4]
                if float(time.monotonic()) - tower.t < 1.0:
                    pygame.draw.circle(window, RED, (tower.rect.centerx, tower.rect.centery), 100, 0)
                else:
                    tower.kill()
            if tower.number == 0:
                del tower.elist[:]

        for bullet in param_dict["missile_list"]:
            bullet.target = [bullet.target_enemy.rect.centerx, bullet.target_enemy.rect.centery]

        for tower in param_dict["tower_list"]:
            if tower.PipeUp == 0:
                tower.x0 = tower.rect.centerx
                tower.y0 = tower.rect.centery - 12
                tower.PipeUp = 1
            pygame.draw.line(window, BLACK, (tower.rect.centerx, tower.rect.centery),
                             (tower.x0, tower.y0), 1)
            if (xpos > (tower.rect.centerx-10) and xpos < (tower.rect.centerx+10) and
                ypos > (tower.rect.centery-10) and ypos < (tower.rect.centery+10)):
                pygame.draw.circle(window, BLUE, (tower.rect.centerx, tower.rect.centery), tower.range, 1)
            for enemy in param_dict["enemy_list"]:
                if (enemy.health <= 0):
                    enemy.kill()
                    player.Money += enemy.price
                enemy.dist = sqrt((enemy.rect.centerx - tower.rect.centerx)**2 +
                                  (enemy.rect.centery - tower.rect.centery)**2)
                if enemy.dist <= tower.range:
                    param_dict["range_list"].append(enemy)
                    param_dict["dictionary"][enemy.value] = enemy
                    param_dict["value_list"].append(enemy.value)
                for bullet in param_dict["bullet_list"]:
                    if pygame.sprite.collide_rect(bullet, enemy):
                        if bullet.type_2 != enemy.resistant:
                            enemy.health -= bullet.damage
                            if bullet.poison == 1 and enemy.poison == 0:
                                enemy.poison = 1
                                enemy.poisonTime = time.monotonic()
                            if bullet.type == 2:
                                if enemy.speed == 2:
                                    enemy.speed = 1
                                if enemy.resistant != 5:
                                    enemy.resistant = 5
                                enemy.image = black_monster
                        bullet.kill()
                for bullet in param_dict["missile_list"]:
                    if pygame.sprite.collide_rect(bullet, enemy):
                        if bullet.type_2 != enemy.resistant:
                            enemy.health -= bullet.damage
                            if bullet.poison == 1 and enemy.poison == 0:
                                enemy.poison = 1
                                enemy.poisonTime = time.monotonic()
                        bullet.kill()
                        
            param_dict["value_list"].sort()
            param_dict["value_list"].reverse()
            if (float(time.monotonic()) - float(tower.beginning) >= tower.interval and
                (param_dict["value_list"])): # Check if enough time has passed from the previous shot so that we can shoot again
                # Set the target to be the enemy that has travelled the longest distance.
                target = [param_dict["dictionary"][param_dict["value_list"][0]].rect.centerx,
                          param_dict["dictionary"][param_dict["value_list"][0]].rect.centery]
                startpoint = [tower.rect.centerx, tower.rect.centery]
                tower.x0 = (startpoint[0] + 12*(target[0]-startpoint[0]) /
                            param_dict["dictionary"][param_dict["value_list"][0]].dist)
                tower.y0 = (startpoint[1] + 12*(target[1]-startpoint[1]) /
                            param_dict["dictionary"][param_dict["value_list"][0]].dist)
                pygame.draw.line(window, BLACK, (startpoint[0], startpoint[1]),
                                 (round(tower.x0), round(tower.y0)), 1)
                damage = tower.damage
                poison = tower.poison
                Type = tower.type
                Type_2 = tower.type_2
                bullet = Bullet(target, startpoint, damage, poison,
                                Type, Type_2,
                                param_dict["dictionary"][param_dict["value_list"][0]])
                if tower.homing == 0:
                    param_dict["bullet_list"].add(bullet)
                elif tower.homing == 1:
                    param_dict["missile_list"].add(bullet)
                tower.beginning = time.monotonic() # The moment when a tower shoots a bullet
            del param_dict["value_list"][:]
            del param_dict["range_list"][:]
            param_dict["dictionary"].clear()
        if (len(param_dict["enemy_list"]) != 0):
            RoundDelta = float(time.monotonic())
        # If it has passed at least 0.6 seconds since the list containing the enemies was cleared,
        # we enable the possibility to press the "start round"-button
        if (float(time.monotonic()) - RoundDelta > 0.6):
            StartRoundFlag = 1

        if (jumpLines == 0 and field.number == 1):
            window.blit(start, (5, 315))
        elif (jumpLines == 0 and field.number == 2):
            window.blit(start, (5, 67))
        elif (jumpLines == 0 and field.number == 3):
            window.blit(start, (570, 670))
        elif (jumpLines == 0 and field.number == 4):
            window.blit(start, (620, 670))
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
