class Maze:

    def __init__(self, filename):
        """ maze creation """
        # opening the text file
        with open(filename, "r") as file:
            structure_maze = []
            #reading the lines
            for line in file:
                lines = []
                # reading the columns
                for sprite in line:
                    if sprite != '\n':
                        # adding the column to the line's list
                        lines.append(sprite)
                # adding the line to the maze's list
                structure_maze.append(lines)
            # implementing the structure
            self.structure = structure_maze

    def display(self):
        """ maze display """
        for line in self.structure:
            # remove the spaces & join the characters
            toto = "".join(line)
            print(toto)

    def get_player_position(self):
        """ getting player position """
        x = 0
        # reading lines & columns
        for line in self.structure:
            y = 0
            for character in line:
                if character == 'P':
                    return x, y
                y += 1
            x += 1

    def get_guard_position(self):
        """ getting guard position """
        x = 0
        # reading lines & columns
        for line in self.structure:
            y = 0
            for character in line:
                if character == 'G':
                    return x, y
                y += 1
            x += 1

    def get_empty_spaces(self):
        """ creating an empty spaces list to allow tools random positioning """
        empty_spaces = []
        # reading lines & columns
        x = 0
        for line in self.structure:
            y = 0
            for character in line:
                if character == ' ':
                    empty_spaces.append((x, y))
                y += 1
            x += 1
        return empty_spaces

    def write_symbol(self, x, y, symbol):
        """ writing the new position after moving """
        self.structure[x][y] = symbol

    def get_symbol(self, x, y):
        """ using the value and not the position to allow value testings """
        return self.structure[x][y]

