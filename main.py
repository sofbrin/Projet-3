#! /usr/bin/env python3
# coding: utf8
import argparse


from Maze import Maze
from Game_Manager import GameManager
from Constants import maze_title, game_intro
from Gui import Gui


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gui", action='store_true',
                        help="""ouverture en mode graphique""")
    return parser.parse_args()


def main():
    """ opening through GUI or Terminal """
    args = parse_arguments()
    labyrinth = Maze("grid.txt")
    if args.gui is True:
        gui = Gui(labyrinth)
        gui.start()

    else:
        print(maze_title)
        print(game_intro)
        game_manager = GameManager(labyrinth)
        game_manager.play_or_quit()


if __name__ == "__main__":
    main()
