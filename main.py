#! /usr/bin/env python3
# coding: utf8

from maze import*
from game_manager import GameManager
from constants import*


if __name__== "__main__":
    print(maze_title)
    print(game_intro)

    labyrinth = Maze("grid.txt")
    game_manager = GameManager(labyrinth)
    game_manager.play_or_quit()

