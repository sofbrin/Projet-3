#! /usr/bin/env python3
# coding: utf8


class Player:

    def __init__(self, x, y):
        """ initializing player's position """
        self.x = x
        self.y = y

        # init picked up tools list
        self.PickedUpTools = []

    def add_tool(self, symbol):
        """ adding picked up tools to list """
        self.PickedUpTools.append(symbol)

        """for tool in self.PickedUpTools:
            for idx, symbol in enumerate(self.symbols):
                if tool == symbol:
                    self.add_tool_text(self.names[idx])"""

    def write_pickedup_tool_name(self):
        """ writing tools' names when picked up """
        print("Objets ramassés : ", ' - '.join([tool for tool in self.PickedUpTools]))

    def moving_up(self):
        self.x -= 1
        return self.x, self.y

    def moving_down(self):
        self.x += 1
        return self.x, self.y

    def moving_right(self):
        self.y += 1
        return self.x, self.y

    def moving_left(self):
        self.y -= 1
        return self.x, self.y

    """def input_choice2(self):
        c = readkey()
        return c

    def moving_to(self):
        player's move

        choice2 = self.input_choice2()

        if choice2 == key.RIGHT:
            self.moving_right()

        elif choice2 == key.LEFT:
            self.moving_left()

        elif choice2 == key.DOWN:
            self.moving_down()

        elif choice2 == key.UP:
            self.moving_up()"""

    def moving_to(self):
        """ player's move """
        while True:
            choice2 = input('Choisissez un chiffre pour vous déplacer : ')
            if choice2 == "Q" or choice2 == "6" or choice2 == "4" \
                    or choice2 == "8" or choice2 == "2":
                break

        if choice2 == "Q":
            return None

        elif choice2 == "6":
            self.moving_right()

        elif choice2 == "4":
            self.moving_left()

        elif choice2 == "8":
            self.moving_up()

        elif choice2 == "2":
            self.moving_down()

        return self.x, self.y

    def __str__(self):
        """ checking if the player's positioning works fine """
        return str(self.x) + " " + str(self.y)

    def set_position(self, position):
        """ sending back to the previous position
            if the new one doesnt allow the move
        """
        self.x = position[0]
        self.y = position[1]