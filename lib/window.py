# dependencies
import os, sys, pygame

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.board import Board

# TODO get some scafolding going

class Window:
    def __init__(self):
        self.sb = Board()

        # TODO make a create sudoku method on board later, 
        # then delete this block
        hard = [
            6,0,0,0,0,0,0,0,8,
            0,4,0,9,0,2,0,3,0,
            0,0,3,0,1,0,4,0,0,
            0,2,0,6,0,5,0,8,0,
            0,0,5,0,0,0,7,0,0,
            0,1,0,7,0,9,0,2,0,
            0,0,4,0,9,0,1,0,0,
            0,3,0,5,0,8,0,6,0,
            7,0,0,0,0,0,0,0,0
        ]
        self.sb.update_board(hard)
    
    # create window

    # create rectangles

    # draw

    # main loop

    # color decider NOTE maybe not needed