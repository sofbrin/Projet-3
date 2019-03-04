import random
import sys


from Player import Player
from Guard import Guard
from Constants import*
from Tool import Tool


class GameManager:

    """ init Game Manager """
    def __init__(self, labyrinth):
        self.labyrinth = labyrinth

        # player & guard positioning
        positionP = self.labyrinth.get_player_position()
        positionG = self.labyrinth.get_guard_position()
        self.MacGyver = Player(positionP[0], positionP[1])
        self.guard = Guard(positionG[0], positionG[1])

        # tools random positioning from an empty spaces list
        empty_spaces = self.labyrinth.get_empty_spaces()
        self.tools = []
        self.symbols = ['E', 'N', 'T']
        self.names = ['Ether', 'Needle', 'Tube']

        for idx, symbol in enumerate(self.symbols):
            tmp_pos = random.choice(empty_spaces)
            temp_tool = Tool(tmp_pos[0], tmp_pos[1], symbol, self.names[idx])
            self.tools.append(temp_tool)
            empty_spaces.remove(tmp_pos)

        for tool in self.tools:
            self.labyrinth.write_symbol((tool.x, tool.y), tool.symbol)

    """ Game loop """
    def play_or_quit(self):

        choice1 = input('Tapez 1 pour jouer, Q pour quitter : ')

        while choice1 == "1":
            self.labyrinth.display()
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

            elif val_new_pos == 'E' or val_new_pos == 'N' or val_new_pos == 'T':
                self.MacGyver.add_tool(val_new_pos)
                self.labyrinth.write_symbol(new_pos, "P")
                self.labyrinth.write_symbol(prev_pos, " ")

            elif val_new_pos == 'G':
                if len(self.MacGyver.PickedUpTools) < 3:
                    print('Arghhhhhh, perdu, il manque {} objets!!!'.format(3 - len(self.MacGyver.PickedUpTools)))
                else:
                    self.labyrinth.write_symbol(new_pos, "P")
                    self.labyrinth.write_symbol(prev_pos, " ")
                    print('Bravo, MacGyver a réussi à sortir du labyrinthe !')
                break

        print(end_of_game)
