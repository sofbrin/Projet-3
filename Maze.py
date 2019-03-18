#! /usr/bin/env python3
# coding: utf8


class Maze:

    def __init__(self, filename):
        """ maze creation """
        with open(filename, "r") as file:
            structure_maze = []
            for line in file:
                lines = []
                for column in line:
                    if column != '\n':
                        lines.append(column)
                structure_maze.append(lines)
            self.structure = structure_maze

    def display(self):
        """ maze display """
        for line in self.structure:
            maze = "".join(line)
            print(maze)

    def get_player_position(self):
        """ getting player's position """
        for x, line in enumerate(self.structure):
            for y, character in enumerate(line):
                if character == 'P':
                    return x, y

    def get_guard_position(self):
        """ getting guard's position """
        for x, line in enumerate(self.structure):
            for y, character in enumerate(line):
                if character == 'G':
                    return x, y

    def get_empty_spaces(self):
        """ creating an empty spaces list to allow tools random positioning """
        empty_spaces = []
        for x, line in enumerate(self.structure):
            for y, character in enumerate(line):
                if character == ' ':
                    empty_spaces.append((x, y))
        return empty_spaces

    def write_symbol(self, position, symbol):
        """ writing the symbol in the new position after moving """
        self.structure[position[0]][position[1]] = symbol

    def get_symbol(self, position):
        """ using the value and not the position to allow value testing """
        return self.structure[position[0]][position[1]]
