#! /usr/bin/env python3
# coding: utf8
import random
import sys


from Player import Player
from Guard import Guard
from Constants import game_instructions, end_of_game
from Tool import Tool


class GameManager:

    def __init__(self, labyrinth):
        """ initializing Game Manager """
        self.labyrinth = labyrinth

        # player & guard positioning
        position_p = self.labyrinth.get_player_position()
        position_g = self.labyrinth.get_guard_position()
        self.MacGyver = Player(position_p[0], position_p[1])
        self.guard = Guard(position_g[0], position_g[1])

        # tools random positioning from an empty spaces list
        empty_spaces = self.labyrinth.get_empty_spaces()
        self.tools = []
        self.symbols = ['E', 'N', 'T']
        self.names = ['éther', 'aiguille', 'tube']

        for idx, symbol in enumerate(self.symbols):
            tmp_pos = random.choice(empty_spaces)
            temp_tool = Tool(tmp_pos[0], tmp_pos[1], symbol, self.names[idx])
            self.tools.append(temp_tool)
            empty_spaces.remove(tmp_pos)

        for tool in self.tools:
            self.labyrinth.write_symbol((tool.x, tool.y), tool.symbol)

    def play_or_quit(self):
        """ Game loop """
        choice1 = input('Tapez 1 pour jouer, Q pour quitter : ')

        while choice1 == "1":
            self.labyrinth.display()
            self.MacGyver.write_pickedup_tool_name()
            print(game_instructions)

            # moving vars definition
            new_pos = self.MacGyver.moving_to()
            if new_pos is None:
                print(end_of_game)
                sys.exit()

            prev_pos = self.labyrinth.get_player_position()
            val_new_pos = self.labyrinth.get_symbol(new_pos)

            # player's moves testing
            if val_new_pos == ' ':
                self.labyrinth.write_symbol(new_pos, "P")
                self.labyrinth.write_symbol(prev_pos, " ")

            elif val_new_pos == 'x':
                self.MacGyver.set_position(prev_pos)
                print("Déplacement impossible")

            elif val_new_pos == 'E' or val_new_pos == 'N' \
                    or val_new_pos == 'T':
                self.MacGyver.add_tool(val_new_pos)
                self.labyrinth.write_symbol(new_pos, "P")
                self.labyrinth.write_symbol(prev_pos, " ")

            elif val_new_pos == 'G':
                if len(self.MacGyver.PickedUpTools) < 3:
                    print('Perdu, il manque {} objet(s)!!!'.
                          format(3 - len(self.MacGyver.PickedUpTools)))
                else:
                    self.labyrinth.write_symbol(new_pos, "P")
                    self.labyrinth.write_symbol(prev_pos, " ")
                    print('Bravo, MacGyver a réussi à sortir du labyrinthe !')
                break

        print(end_of_game)

    """def print_tool_name(self):
        #for tool in self.MacGyver.PickedUpTools:
        for idx, symbol in enumerate(self.symbols):
                #if tool == symbol:
            print('Objet(s) ramassé(s) : ', ', '.join(self.names[idx] for tool in self.MacGyver.PickedUpTools))
            #{}'.format(self.names[idx]))"""
