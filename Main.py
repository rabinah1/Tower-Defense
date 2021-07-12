import pygame
import sys
import time
from pygame.locals import QUIT, K_ESCAPE
from Player import Player
from Map import Map
from Road import Piece
from Environment_sprite import Environment
from Functions import (set_weapon, Initialize, draw_menu, draw_game_static, read,
                       draw_while_update, guide, update_enemies,
                       process_contact_bombs, process_range_bombs, process_towers)
from common import BLACK, WHITE


def menu():
    pygame.init()
    window = pygame.display.set_mode((1500, 700))
    pygame.display.set_caption("Tower Defense")
    menu_font = pygame.font.SysFont("Calibri", 45, True, False)
    menu_text = menu_font.render("Menu", True, BLACK)
    param_dict = Initialize()
    font = pygame.font.SysFont("Calibri", 18, True, False)
    start = font.render("Start", True, BLACK)
    exit_flag = False
    clock = pygame.time.Clock()
    draw_menu(window, param_dict)
    while True:
        pos = pygame.mouse.get_pos()
        xpos = pos[0]
        ypos = pos[1]
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 780 and xpos < 900 and
                  ypos > 600 and ypos < 670):  # User clicks on the EXIT-button
                pygame.quit()
                sys.exit()

            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 380 and xpos < 695 and
                  ypos > 595 and ypos < 670):  # User clicks on the INSTRUCTIONS-button
                guide(window)
                draw_menu(window, param_dict)

            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 70 and xpos < 500 and
                  ypos > 30 and ypos < 250):  # User clicks on the map on the top left corner
                field = Map(1)
                table_id = "1"
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

                player = Player(0, 400, 20)
                # Add environment textures to a list called "environment_list".
                environment_list.add(Environment(param_dict["tree"], 10, 550))
                environment_list.add(Environment(param_dict["tree"], 250, 500))
                environment_list.add(Environment(param_dict["tree"], 990, 300))
                environment_list.add(Environment(param_dict["tree_2"], 1090, 585))
                environment_list.add(Environment(param_dict["lake"], 270, 230))
                environment_list.add(Environment(param_dict["tree_2"], 600, 200))
                environment_list.add(Environment(param_dict["tree"], 600, 400))
                exit_flag = True
                break

            # User clicks on the map on the top right corner
            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 1000 and xpos < 1430 and
                  ypos > 30 and ypos < 250):
                field = Map(2)
                table_id = "2"
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

                player = Player(0, 400, 20)

                environment_list.add(Environment(param_dict["lake"], 535, 15))
                environment_list.add(Environment(param_dict["tree"], 10, 580))
                environment_list.add(Environment(param_dict["tree_2"], 40, 400))
                environment_list.add(Environment(param_dict["tree"], 700, 140))
                environment_list.add(Environment(param_dict["tree"], 650, 340))
                environment_list.add(Environment(param_dict["tree_2"], 400, 50))
                environment_list.add(Environment(param_dict["lake"], 190, 380))
                exit_flag = True
                break

            # User clicks on the map on the lower left corner
            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 70 and xpos < 500 and
                  ypos > 300 and ypos < 520):
                field = Map(3)
                table_id = "3"
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

                player = Player(0, 600, 20)

                environment_list.add(Environment(param_dict["lake"], 1000, 20))
                environment_list.add(Environment(param_dict["tree_2"], 850, 20))
                environment_list.add(Environment(param_dict["tree"], 650, 50))
                environment_list.add(Environment(param_dict["lake"], 400, 50))
                environment_list.add(Environment(param_dict["tree"], 20, 570))
                environment_list.add(Environment(param_dict["tree_2"], 1100, 570))
                environment_list.add(Environment(param_dict["tree"], 50, 90))
                environment_list.add(Environment(param_dict["tree_2"], 170, 370))
                exit_flag = True
                break

            # User clicks on the map on the lower right corner
            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 1000 and xpos < 1430 and
                  ypos > 300 and ypos < 520):
                field = Map(4)
                table_id = "4"
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

                player = Player(0, 600, 20)

                environment_list.add(Environment(param_dict["tree"], 50, 530))
                environment_list.add(Environment(param_dict["tree"], 1050, 530))
                environment_list.add(Environment(param_dict["lake"], 210, 200))
                environment_list.add(Environment(param_dict["tree_2"], 930, 210))
                environment_list.add(Environment(param_dict["tree"], 800, 210))
                environment_list.add(Environment(param_dict["tree_2"], 210, 70))
                environment_list.add(Environment(param_dict["tree"], 570, 430))
                exit_flag = True
                break

        if exit_flag:
            exit_flag = False
            main(pieces_list, player, field, environment_list, table_id, window, param_dict,
                 start, menu_text)
            draw_menu(window, param_dict)

        pygame.display.update()
        clock.tick(60)


def main(pieces_list, player, field, environment_list, table_id, window,
         param_dict, start, menu_text):
    clock = pygame.time.Clock()
    database = "Map1.db"
    round_stats = []  # A list that contains the information of all enemies of a certain round
    round_idx = -1  # A variable used for indexing the round_stats-list
    delta = 0  # How frequently new enemies are created to the game field
    jump_rounds = 0  # Explained in the function "read_file"
    start_round_flag = 1
    round_delta = 0
    while True:
        pos = pygame.mouse.get_pos()
        xpos = pos[0]
        ypos = pos[1]
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Select machine gun tower
            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1420 and ypos < 80:
                (tower, round_stats, delta, round_idx) = \
                    set_weapon(param_dict, window, pieces_list, round_stats, delta, round_idx,
                               player, start, field, jump_rounds, environment_list, "machine_gun")
                if (tower, round_stats, delta, round_idx) == (None, None, None, None):
                    return
                if tower is not None:
                    param_dict["tower_list"].add(tower)

            # Select shotgun tower
            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1340 and xpos < 1420 and ypos < 80:
                (tower, round_stats, delta, round_idx) = \
                    set_weapon(param_dict, window, pieces_list, round_stats, delta, round_idx,
                               player, start, field, jump_rounds, environment_list, "shotgun")
                if (tower, round_stats, delta, round_idx) == (None, None, None, None):
                    return
                if tower is not None:
                    param_dict["tower_list"].add(tower)

            # Select assistant tower
            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1260 and xpos < 1340 and ypos < 80:
                (tower, round_stats, delta, round_idx) = \
                    set_weapon(param_dict, window, pieces_list, round_stats, delta, round_idx,
                               player, start, field, jump_rounds, environment_list, "assistant")
                if (tower, round_stats, delta, round_idx) == (None, None, None, None):
                    return
                if tower is not None:
                    param_dict["tower_list"].add(tower)

            # Select pistol tower
            elif event.type == pygame.MOUSEBUTTONDOWN and xpos > 1180 and xpos < 1260 and ypos < 80:
                (tower, round_stats, delta, round_idx) = \
                    set_weapon(param_dict, window, pieces_list, round_stats, delta, round_idx,
                               player, start, field, jump_rounds, environment_list, "pistol")
                if (tower, round_stats, delta, round_idx) == (None, None, None, None):
                    return
                if tower is not None:
                    param_dict["tower_list"].add(tower)

            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 1180 and xpos < 1260 and
                  ypos < 192 and ypos > 112):  # Select mine
                (tower, round_stats, delta, round_idx) = \
                    set_weapon(param_dict, window, pieces_list, round_stats, delta, round_idx,
                               player, start, field, jump_rounds, environment_list, "mine")
                if (tower, round_stats, delta, round_idx) == (None, None, None, None):
                    return
                if tower is not None:
                    param_dict["contact_bomb_list"].add(tower)

            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 1260 and xpos < 1340 and
                  ypos < 192 and ypos > 112):  # Select smart bomb
                (tower, round_stats, delta, round_idx) = \
                    set_weapon(param_dict, window, pieces_list, round_stats, delta, round_idx,
                               player, start, field, jump_rounds, environment_list, "smart_bomb")
                if (tower, round_stats, delta, round_idx) == (None, None, None, None):
                    return
                if tower is not None:
                    param_dict["range_bomb_list"].add(tower)

            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 1340 and xpos < 1420 and
                  ypos < 192 and ypos > 112):  # Select homing missile
                (tower, round_stats, delta, round_idx) = \
                    set_weapon(param_dict, window, pieces_list, round_stats, delta, round_idx,
                               player, start, field, jump_rounds, environment_list,
                               "homing_missile")
                if (tower, round_stats, delta, round_idx) == (None, None, None, None):
                    return
                if tower is not None:
                    param_dict["tower_list"].add(tower)

            elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:  # Pause the game
                pygame.draw.rect(window, WHITE, (1180, 602, 1500, 700), 0)
                window.blit(menu_text, (1280, 630))
                diff = float(time.monotonic()) - delta
                while True:
                    n = 0
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                            n = 1
                            break
                        # Player clicks on the "MENU"-button
                        elif (event.type == pygame.MOUSEBUTTONDOWN and
                              pygame.mouse.get_pos()[0] > 1180 and
                              pygame.mouse.get_pos()[1] > 600):
                            param_dict["tower_list"].empty()
                            param_dict["bullet_list"].empty()
                            param_dict["enemy_list"].empty()
                            param_dict["dictionary"].clear()
                            param_dict["contact_bomb_list"].empty()
                            param_dict["range_bomb_list"].empty()
                            param_dict["missile_list"].empty()
                            del param_dict["range_list"][:]
                            del param_dict["value_list"][:]
                            return
                        elif event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        pygame.display.update()
                        clock.tick(60)
                    if n == 1:
                        delta = float(time.monotonic()) - diff
                        break

            # Player clicks on the "START ROUND"-button
            elif (event.type == pygame.MOUSEBUTTONDOWN and xpos > 1180 and
                  ypos > 600 and start_round_flag == 1):
                round_stats = read(field, table_id, jump_rounds, player, window, database)
                if round_stats[0] == "RET":
                    param_dict["tower_list"].empty()
                    param_dict["bullet_list"].empty()
                    param_dict["enemy_list"].empty()
                    param_dict["dictionary"].clear()
                    param_dict["contact_bomb_list"].empty()
                    param_dict["range_bomb_list"].empty()
                    param_dict["missile_list"].empty()
                    del param_dict["range_list"][:]
                    del param_dict["value_list"][:]
                    return
                jump_rounds += 1
                delta = float(time.monotonic())
                round_idx = 0
                start_round_flag = 0
                round_delta = float(time.monotonic())

            for tower in param_dict["tower_list"]:  # Loop through all towers
                if (event.type == pygame.MOUSEBUTTONDOWN and xpos > (tower.rect.centerx-10) and
                   xpos < (tower.rect.centerx+10) and ypos > (tower.rect.centery-10) and
                   ypos < (tower.rect.centery+10)):
                    (tower, round_stats, delta, round_idx) = \
                        draw_while_update(param_dict, window, pieces_list, round_stats, delta,
                                          round_idx, tower, player, start, field, jump_rounds,
                                          environment_list, True)
                    if (tower, round_stats, delta, round_idx) == (None, None, None, None):
                        return

            for tower in param_dict["contact_bomb_list"]:  # Loop through all mines
                if (event.type == pygame.MOUSEBUTTONDOWN and xpos > (tower.rect.centerx-10) and
                   xpos < (tower.rect.centerx+10) and ypos > (tower.rect.centery-10) and
                   ypos < (tower.rect.centery+10)):
                    (tower, round_stats, delta, round_idx) = \
                        draw_while_update(param_dict, window, pieces_list, round_stats, delta,
                                          round_idx, tower, player, start, field, jump_rounds,
                                          environment_list, False)
                    if (tower, round_stats, delta, round_idx) == (None, None, None, None):
                        return

            for tower in param_dict["range_bomb_list"]:  # Loop through all smart bombs
                if (event.type == pygame.MOUSEBUTTONDOWN and xpos > (tower.rect.centerx-10) and
                   xpos < (tower.rect.centerx+10) and ypos > (tower.rect.centery-10) and
                   ypos < (tower.rect.centery+10)):
                    (tower, round_stats, delta, round_idx) = \
                        draw_while_update(param_dict, window, pieces_list, round_stats, delta,
                                          round_idx, tower, player, start, field, jump_rounds,
                                          environment_list, False)
                    if (tower, round_stats, delta, round_idx) == (None, None, None, None):
                        return

        if (float(time.monotonic()) - delta > 0.5 and round_idx < len(round_stats) and
           round_idx != -1):
            param_dict["enemy_list"].add(round_stats[round_idx])
            delta = float(time.monotonic())
            if len(round_stats) - round_idx == 1:
                del round_stats[:]
                round_idx = -1
            else:
                round_idx += 1
        draw_game_static(window, param_dict, pieces_list, player, environment_list)
        param_dict["tower_list"].draw(window)
        param_dict["contact_bomb_list"].draw(window)
        param_dict["range_bomb_list"].draw(window)

        if (update_enemies(param_dict, window, player) == "return_menu"):
            return
        process_contact_bombs(param_dict, xpos, ypos, window, True)
        process_range_bombs(param_dict, xpos, ypos, window, True)
        process_towers(param_dict, xpos, ypos, window, True)

        if (len(param_dict["enemy_list"]) != 0):
            round_delta = float(time.monotonic())
        # If it has passed at least 0.6 seconds since the list containing the enemies was cleared,
        # we enable the possibility to press the "start round"-button
        if (float(time.monotonic()) - round_delta > 0.6):
            start_round_flag = 1

        if (jump_rounds == 0 and field.map_number == 1):
            window.blit(start, (5, 315))
        elif (jump_rounds == 0 and field.map_number == 2):
            window.blit(start, (5, 67))
        elif (jump_rounds == 0 and field.map_number == 3):
            window.blit(start, (570, 670))
        elif (jump_rounds == 0 and field.map_number == 4):
            window.blit(start, (620, 670))
        param_dict["bullet_list"].update()
        param_dict["enemy_list"].update()
        param_dict["missile_list"].update()
        param_dict["bullet_list"].draw(window)
        param_dict["enemy_list"].draw(window)
        param_dict["missile_list"].draw(window)
        param_dict["dictionary"].clear()
        del param_dict["value_list"][:]
        del param_dict["range_list"][:]
        pygame.display.update()
        clock.tick(60)


menu()
