class Maze:

    """ maze creation """
    def __init__(self, filename):

        # opening the text file
        with open(filename, "r") as file:
            structure_maze = []
            # reading the lines
            for line in file:
                lines = []
                # reading the columns
                for sprite in line:
                    if sprite != '\n':
                        # adding the column to the lines' list
                        lines.append(sprite)
                # adding the line to the maze's list
                structure_maze.append(lines)
            # implementing the structure
            self.structure = structure_maze

    """ maze display """
    def display(self):
        for line in self.structure:
            # remove the spaces & join the characters
            toto = "".join(line)
            print(toto)

    """ getting player's position """
    def get_player_position(self):
        x = 0
        # reading lines & columns
        for line in self.structure:
            y = 0
            for character in line:
                if character == 'P':
                    return x, y
                y += 1
            x += 1

    """ getting guard's position """
    def get_guard_position(self):
        x = 0
        # reading lines & columns
        for line in self.structure:
            y = 0
            for character in line:
                if character == 'G':
                    return x, y
                y += 1
            x += 1

    """ creating an empty spaces list to allow tools random positioning """
    def get_empty_spaces(self):
        empty_spaces = []
        x = 0
        # reading lines & columns
        for line in self.structure:
            y = 0
            for character in line:
                if character == ' ':
                    empty_spaces.append((x, y))
                y += 1
            x += 1
        return empty_spaces

    """ writing the new position after moving """
    def write_symbol(self, position, symbol):
        self.structure[position[0]][position[1]] = symbol

    """ using the value and not the position to allow value testing """
    def get_symbol(self, position):
        return self.structure[position[0]][position[1]]

