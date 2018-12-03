""" Grid parameters """

sprite_side_number = 15
sprite_size = 30
board_side = sprite_side_number * sprite_size

board_title = "Le labyrinthe de MacGyver"

class Board:

    def __init__(self, file):
        self.file = file
        self.structure = 0

    """ board creation """
    def build_grid(self):
        
        # ouverture du fichier texte
        with open("grid.txt", "r") as file:
            structure_board = []
            
            #parcourir les lignes
            for line in file:
                lines = []

                #parcourir les sprites
                for sprite in line:
                    #considérer les sauts de ligne
                    if sprite != '\n':
                        # ajouter le sprite à la liste de la ligne
                        lines.append(sprite)
                # ajouter la ligne à la liste du plateau
                structure_board.append(lines)
            # implémenter la structure
            self.structure = structure_board

    """ board display """
    def display(self, board):

        # parcourir la liste du plateau
        line_number = 0
        for line in self.structure:
            # parcourir les listes de lignes
            box_number = 0
            for sprite in line:
                x = box_number * sprite_size
                y = line_number * sprite_size

                if sprite == 'w':       # w = wall
                    board.blit(wall, (x,y))
                
                elif sprite == 'S':     # S = start
                    board.blit(start, (x,y))
                
                elif sprite == 'E':     # E = end
                    board.blit(end, (x,y))

                elif sprite =='G':      # G = guard
                    board.blit(guard, (x,y))

                box_number += 1
            line_number += 1


