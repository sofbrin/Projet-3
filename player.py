class Player:

    """ init player's position """
    def __init__(self, x, y):
        self.x = x
        self.y = y

        """ init picked up tools list """
        self.PickedUpTools = []

    """ adding picked up tools to list """
    def add_tool(self, symbol):
        self.PickedUpTools.append(symbol)

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

    """ moving the player """
    def moving_to(self):
        while True:
            choice2 = input('Choisissez un chiffre pour vous déplacer : ')
            if choice2 == "Q" or choice2 == "6" or choice2 == "4" or choice2 == "8" or choice2 == "2":
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

    """ checking if the player's positioning works fine """
    def __str__(self):
        return str(self.x) + " " + str(self.y)

    """ sending back to the previous position if the new one doesnt allow the move """
    def set_position(self, position):
        self.x = position[0]
        self.y = position[1]
