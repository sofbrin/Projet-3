#! /usr/bin/env python3
# coding: utf8


class Tool:

    def __init__(self, x, y, symbol, name, image=None):
        """ initializing tools """
        self.x = x
        self.y = y
        self.symbol = symbol
        self.name = name
        self.image = image
