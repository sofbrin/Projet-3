from constants import*


class Player:

    def __init__(self, x, y):
        """ init player's position """
        self.x = x
        self.y = y

        """ init picked up tools list """
        self.PickedUpTools = []

    def add_tools(self, symbol):
        """ adding picked up tools to list """
        self.PickedUpTools.append(symbol)

    def moving_to(self):
        """ moving the player """
        choice2 = input('Choisissez un chiffre pour vous déplacer : ')

        if choice2 == "Q":
            print(end_of_game)

        elif choice2 == "6":
            self.y += 1

        elif choice2 == "4":
            self.y -= 1

        elif choice2 == "8":
            self.x -= 1

        elif choice2 == "2":
            self.x += 1

        return self.x, self.y


    def __str__(self):
        """ checking if the player's positioning works fine """
        return str(self.x) + " " + str(self.y)

    def set_position(self, position):
        """ sending back to the previous position if the new one doesnt allow the move """
        self.x = position[0]
        self.y = position[1]

