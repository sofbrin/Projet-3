#! /usr/bin/env python3
# coding: utf8
import pygame
import random
import sys

from pygame.locals import K_RIGHT, K_LEFT, K_DOWN, K_UP
from Player import Player
from Tool import Tool


class ImageSprite(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.rect.x = y * 40
        self.rect.y = x * 40


class Gui:

    def __init__(self, labyrinth):
        self.labyrinth = labyrinth

        # Player positioning
        position_p = self.labyrinth.get_player_position()
        self.MacGyver = Player(position_p[0], position_p[1])

        # GUI elements initializing
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        self.background_image = pygame.image.load(r"img/background.png")
        self.ether_image = pygame.image.load(r"img/ether.png")
        self.guard_image = pygame.image.load(r"img/guard.png")
        self.macgyver_image = pygame.image.load(r"img/macgyver.png")
        self.needle_image = pygame.image.load(r"img/needle.png")
        self.tube_image = pygame.image.load(r"img/tube.png")
        self.wall_image = pygame.image.load(r"img/wall.png")
        self.win_image = pygame.image.load(r"img/win.png")
        self.lost_image = pygame.image.load(r"img/lost.png")
        self.title_image = pygame.image.load(r"img/title.png")
        self.etherC_image = pygame.image.load(r"img/etherC.png")
        self.needleC_image = pygame.image.load(r"img/needleC.png")
        self.tubeC_image = pygame.image.load(r"img/tubeC.png")
        self.clock = pygame.time.Clock()

        self.character_sprites_list = pygame.sprite.Group()
        self.tools_sprites_list = pygame.sprite.Group()
        self.wall_sprites_list = pygame.sprite.Group()

        self.macgyver_sprite = ImageSprite(self.macgyver_image)
        self.guard_sprite = ImageSprite(self.guard_image)
        self.tools_list = (ImageSprite(self.ether_image),
                           ImageSprite(self.needle_image),
                           ImageSprite(self.tube_image))

        self.character_sprites_list.add([self.macgyver_sprite,
                                         self.guard_sprite])
        self.tools_sprites_list.add(self.tools_list)

        # To be used when printing tool's names & icons in lateral
        self.start_tools_y = 200
        self.start_icons_y = 200

        pygame.display.set_caption("Le labyrinthe de MacGyver")

        # Tools random positioning from an empty spaces list
        empty_spaces = self.labyrinth.get_empty_spaces()
        self.tools = []
        self.symbols = ['E', 'N', 'T']
        self.names = ['Ether', 'Aiguille', 'Tube']
        self.images = [self.etherC_image, self.needleC_image, self.tubeC_image]

        for idx, symbol in enumerate(self.symbols):
            tmp_pos = random.choice(empty_spaces)
            temp_tool = Tool(tmp_pos[0], tmp_pos[1], symbol,
                             self.names[idx], self.images[idx])
            self.tools.append(temp_tool)
            empty_spaces.remove(tmp_pos)

        for tool in self.tools:
            self.labyrinth.write_symbol((tool.x, tool.y), tool.symbol)

    def start(self):
        """ Giving the choice: play or quit """
        self.intro_to_game()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN
                         and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    return

                elif event.type == pygame.KEYDOWN:
                    self.launch_game()
                    return

    def intro_to_game(self):
        """ First page: instructions """
        self.screen.blit(self.title_image, [230, 50])
        self.intro_text()
        pygame.display.flip()

    def launch_game(self):
        """ Second page: launching the game """
        self.display_images()

        # Main loop
        pygame.key.set_repeat()
        while True:
            new_pos = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN
                         and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN and event.key == K_RIGHT:
                    new_pos = self.MacGyver.moving_right()
                elif event.type == pygame.KEYDOWN and event.key == K_LEFT:
                    new_pos = self.MacGyver.moving_left()
                elif event.type == pygame.KEYDOWN and event.key == K_DOWN:
                    new_pos = self.MacGyver.moving_down()
                elif event.type == pygame.KEYDOWN and event.key == K_UP:
                    new_pos = self.MacGyver.moving_up()

            # Player's moves testing
            if new_pos is not None:
                prev_pos = self.labyrinth.get_player_position()
                val_new_pos = self.labyrinth.get_symbol(new_pos)

                if val_new_pos == ' ':
                    self.macgyver_sprite.move(new_pos[0], new_pos[1])
                    self.labyrinth.write_symbol(new_pos, "P")
                    self.labyrinth.write_symbol(prev_pos, " ")

                elif val_new_pos == 'x':
                    self.MacGyver.set_position(prev_pos)

                elif val_new_pos == 'E' or val_new_pos == 'N' \
                        or val_new_pos == 'T':
                    self.macgyver_sprite.move(new_pos[0], new_pos[1])
                    self.MacGyver.add_tool(val_new_pos)
                    self.labyrinth.write_symbol(new_pos, "P")
                    self.labyrinth.write_symbol(prev_pos, " ")

                    # Loop to remove the tool from tools' list when picked up
                    for idx, symbol in enumerate(self.symbols):
                        if val_new_pos == symbol:
                            self.tools_list[idx].kill()
                            break

                elif val_new_pos == 'G':
                    self.macgyver_sprite.move(new_pos[0], new_pos[1])
                    if len(self.MacGyver.PickedUpTools) < 3:
                        self.screen.blit(self.lost_image, [0, 0])
                        self.lost_text()
                        pygame.display.flip()
                        pygame.time.wait(5000)
                        sys.exit()
                    else:
                        self.labyrinth.write_symbol(new_pos, "P")
                        self.labyrinth.write_symbol(prev_pos, " ")
                        self.screen.blit(self.win_image, [0, 0])
                        self.win_text()
                        pygame.display.flip()
                        pygame.time.wait(5000)
                    break

                self.display_images()
            self.clock.tick(60)

    def display_images(self):
        """ Images to be called when game loop iteration """
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background_image, [0, 0])
        self.draw_walls()
        self.draw_character()
        self.draw_tools()
        self.lateral_text()
        pygame.display.flip()

    def intro_text(self):
        """ First page text """
        basicfont = pygame.font.SysFont(None, 30)
        text1 = basicfont.render("Pour sortir du labyrinthe, présentez-vous "
                                 "devant le gardien", True, (255, 255, 255))
        text2 = basicfont.render("avec les 3 objets que vous aurez ramassés.",
                                 True, (255, 255, 255))
        text3 = basicfont.render("Vous avez perdu si vous n'avez pas "
                                 "les 3 objets :", True, (255, 255, 255))
        text4 = basicfont.render("L'éther :", True, (255, 255, 255))
        text5 = basicfont.render("L'aiguille :", True, (255, 255, 255))
        text6 = basicfont.render("Le tube :", True, (255, 255, 255))
        text7 = basicfont.render("Utilisez les flèches pour vous déplacer "
                                 "dans le labyrinthe.", True, (255, 255, 255))
        text8 = basicfont.render('Tapez "Echap" pour quitter, n\'importe '
                                 'quelle autre touche pour jouer',
                                 True, (60, 117, 128))

        text1_rect = text1.get_rect()
        text1_rect.x = 50
        text1_rect.y = 200

        text2_rect = text2.get_rect()
        text2_rect.x = 50
        text2_rect.y = 230

        text3_rect = text3.get_rect()
        text3_rect.x = 50
        text3_rect.y = 260

        text4_rect = text4.get_rect()
        text4_rect.x = 50
        text4_rect.y = 300

        text5_rect = text5.get_rect()
        text5_rect.x = 250
        text5_rect.y = 300

        text6_rect = text6.get_rect()
        text6_rect.x = 480
        text6_rect.y = 300

        text7_rect = text7.get_rect()
        text7_rect.x = 50
        text7_rect.y = 400

        text8_rect = text8.get_rect()
        text8_rect.x = 50
        text8_rect.y = 450

        self.screen.blit(text1, text1_rect)
        self.screen.blit(text2, text2_rect)
        self.screen.blit(text3, text3_rect)
        self.screen.blit(text4, text4_rect)
        self.screen.blit(text5, text5_rect)
        self.screen.blit(text6, text6_rect)
        self.screen.blit(text7, text7_rect)
        self.screen.blit(text8, text8_rect)

        self.screen.blit(self.etherC_image, [150, 290])
        self.screen.blit(self.needleC_image, [370, 290])
        self.screen.blit(self.tubeC_image, [590, 290])

    def lateral_text(self):
        """ Second page text """
        basicfont = pygame.font.SysFont(None, 25)
        text1 = basicfont.render("Utilisez les flèches ",
                                 True, (255, 255, 255))
        text2 = basicfont.render("pour vous déplacer",
                                 True, (255, 255, 255))
        text3 = basicfont.render("Vos objets ramassés :",
                                 True, (255, 255, 255))
        text4 = basicfont.render("1.", True, (255, 255, 255))
        text5 = basicfont.render("2.", True, (255, 255, 255))
        text6 = basicfont.render("3.", True, (255, 255, 255))

        text1_rect = text1.get_rect()
        text1_rect.x = 610
        text1_rect.y = 50

        text2_rect = text2.get_rect()
        text2_rect.x = 610
        text2_rect.y = 70

        text3_rect = text3.get_rect()
        text3_rect.x = 610
        text3_rect.y = 150

        text4_rect = text4.get_rect()
        text4_rect.x = 610
        text4_rect.y = 200

        text5_rect = text5.get_rect()
        text5_rect.x = 610
        text5_rect.y = 250

        text6_rect = text6.get_rect()
        text6_rect.x = 610
        text6_rect.y = 300

        self.screen.blit(text1, text1_rect)
        self.screen.blit(text2, text2_rect)
        self.screen.blit(text3, text3_rect)
        self.screen.blit(text4, text4_rect)
        self.screen.blit(text5, text5_rect)
        self.screen.blit(text6, text6_rect)

        # Printing tool's name and image in lateral when picked up
        self.start_tools_y = 200
        self.start_icons_y = 190
        for tool in self.MacGyver.PickedUpTools:
            for idx, symbol in enumerate(self.symbols):
                if tool == symbol:
                    self.add_tool_text(self.names[idx])
                    for t in self.tools:
                        if t.symbol == symbol:
                            self.add_tool_icon(t.image)

    def draw_walls(self):
        """ Building maze: walls """
        for x, line in enumerate(self.labyrinth.structure):
            for y, char in enumerate(line):
                if char == 'x':
                    wall = ImageSprite(self.wall_image)
                    wall.rect.x = y * 40
                    wall.rect.y = x * 40
                    self.wall_sprites_list.add(wall)
        self.wall_sprites_list.draw(self.screen)

    def draw_character(self):
        """ Building maze: characters """
        pos_player = self.labyrinth.get_player_position()
        pos_guard = self.labyrinth.get_guard_position()
        self.macgyver_sprite.move(pos_player[0], pos_player[1])
        self.guard_sprite.move(pos_guard[0], pos_guard[1])
        self.character_sprites_list.update()
        self.character_sprites_list.draw(self.screen)

    def draw_tools(self):
        """ Building maze: tools """
        for idx, temp_tool in enumerate(self.tools):
            self.tools_list[idx].rect.x = temp_tool.y * 40
            self.tools_list[idx].rect.y = temp_tool.x * 40
        self.tools_sprites_list.update()
        self.tools_sprites_list.draw(self.screen)

    def lost_text(self):
        """ Text to be printed in lateral if lost game """
        basicfont = pygame.font.SysFont(None, 20)
        text = basicfont.render("Perdu, il manque {} objet(s) !!!"
                                .format(3 - len(self.MacGyver.PickedUpTools)),
                                True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.x = 610
        text_rect.y = 350
        self.screen.blit(text, text_rect)

    def win_text(self):
        """ Text to be printed in lateral if won game """
        basicfont = pygame.font.SysFont(None, 30)
        text = basicfont.render("Gagné !", True, (255, 215, 0))
        text_rect = text.get_rect()
        text_rect.x = 610
        text_rect.y = 370
        self.screen.blit(text, text_rect)

    def add_tool_text(self, name):
        """ Tool's name text to be printed in lateral when picked up """
        basicfont = pygame.font.SysFont(None, 25)
        text = basicfont.render(name, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = 630
        text_rect.y = self.start_tools_y
        self.screen.blit(text, text_rect)
        self.start_tools_y += 50

    def add_tool_icon(self, image):
        """ Tool's icon to be displayed in lateral when picked up """
        image_rect = image.get_rect()
        image_rect.x = 720
        image_rect.y = self.start_icons_y
        self.screen.blit(image, image_rect)
        self.start_icons_y += 50
