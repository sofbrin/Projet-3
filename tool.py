class Tool:

    """ init tools """
    def __init__(self, x, y, symbol, name): #, image):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.name = name
        #self.image = image

    def __str__(self):
        return self.name
