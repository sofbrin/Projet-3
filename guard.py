#! /usr/bin/env python3
# coding: utf8


class Guard:

    def __init__(self, x, y):
        """ initializing guard's position """
        self.x = x
        self.y = y

    def __str__(self):
        """ checking if the positioning works fine """
        return str(self.x) + " " + str(self.y)
