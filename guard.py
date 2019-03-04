class Guard:

    # init guard's position
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # checking if the positioning works fine
    def __str__(self):
        return str(self.x) + " " + str(self.y)

