import random

from maze import*
from player import Player
from guard import Guard
from constants import*
from tools import Tool


class GameManager:

    def __init__(self, labyrinth):
    """ init Game Manager """
        self.labyrinth = labyrinth

        # player and guard positioning
        positionP = self.labyrinth.get_player_position()
        positionG = self.labyrinth.get_guard_position()
        self.MacGyver = Player(positionP[0], positionP[1])
        self.guard = Guard(positionG[0], positionG[1])

        # tools random positioning from an empty spaces list
        empty_spaces = self.labyrinth.get_empty_spaces()
        self.tools = []
        self.symbols = ['E', 'N', 'T']

        for symbol in self.symbols: # random process
            tmp_pos = random.choice(empty_spaces)
            temp_tool = Tool(tmp_pos[0], tmp_pos[1], symbol)
            self.tools.append(temp_tool)
            empty_spaces.remove(tmp_pos)

        for tool in self.tools: # positionning
            self.labyrinth.write_symbol(tool.x, tool.y, tool.symbol)

        # init picked up tools list
        self.MacGyver.PickedUpTools = []

    def play_or_quit(self):
        """ game loop """

        choice1 = input('Tapez 1 pour jouer, Q pour quitter : ')

        while choice1 == "1":
            self.labyrinth.display()
            print(game_instructions)
            
            # moving vars definition
            new_pos = self.MacGyver.moving_to()
            prev_pos = self.labyrinth.get_player_position()
            val_new_pos = self.labyrinth.get_symbol(new_pos[0], new_pos[1])

            # moving testing
            if val_new_pos == ' ':
                self.labyrinth.write_symbol(new_pos[0], new_pos[1], "P")
                self.labyrinth.write_symbol(prev_pos[0], prev_pos[1], " ")

            if val_new_pos == 'x':
                self.MacGyver.set_position(prev_pos)
                print("Déplacement impossible")

            elif val_new_pos == 'E':
                self.MacGyver.add_tools(['E'])
                self.labyrinth.write_symbol(new_pos[0], new_pos[1], "P")
                self.labyrinth.write_symbol(prev_pos[0], prev_pos[1], " ")

            elif val_new_pos == 'N':
                self.MacGyver.add_tools(['N'])
                self.labyrinth.write_symbol(new_pos[0], new_pos[1], "P")
                self.labyrinth.write_symbol(prev_pos[0], prev_pos[1], " ")

            elif val_new_pos == 'T':
                self.MacGyver.add_tools(['T'])
                self.labyrinth.write_symbol(new_pos[0], new_pos[1], "P")
                self.labyrinth.write_symbol(prev_pos[0], prev_pos[1], " ")

            elif val_new_pos == 'G':
                if len(self.MacGyver.PickedUpTools) < 3:
                    print('Arghhhh, vous n\'avez pas tous les accessoires pour endormir le gardien. C\'est perdu !!!')
                else:
                    self.labyrinth.write_symbol(new_pos[0], new_pos[1], "P")
                    self.labyrinth.write_symbol(prev_pos[0], prev_pos[1], " ")
                    print('Bravo, MacGyver a réussi à sortir du labyrinthe !')
                break

        print(end_of_game)


        
            


       
