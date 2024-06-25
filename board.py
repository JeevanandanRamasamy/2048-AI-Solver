import numpy as np

# Description: This file contains the board class which is used to represent the game board.
class board:
    # Constructor
    def __init__(self):
        self.arr = np.empty((4, 4), dtype=object)
        print(self.arr)
    
    def shift_up(self):
        pass
    
    def shift_down(self):
        pass

    def shift_left(self):
        pass

    def shift_right(self):
        pass
    
    # Method to merge two blocks into one
    def merge(self, loc1, loc2):
        pass
    
board1 = board()