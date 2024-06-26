import numpy as np

# Description: This file contains the board class which is used to represent the 4x4 grid for the 2048 game.
class Board:
    # Constructor
    def __init__(self, size=4):
        # Initialize the board as an empty 4x4 numpy array of objects
        self.arr = np.empty((size, size), dtype=object)
        self.size = size
        self.score = 0
        # Add two random blocks to the board
        self.add_block()
        self.add_block()

    # Adds a random block to the board
    def add_block(self):
        # Find all empty blocks
        empty_blocks = np.where(self.arr == None)
        # Choose a random empty block
        index = np.random.randint(0, len(empty_blocks[0]))
        # Add a 2 or 4 to the block
        self.arr[empty_blocks[0][index], empty_blocks[1][index]] = int(np.random.choice([2, 4]))
    
    # Shifts the board up and merges blocks
    def shift_up(self):
        moved = False
        for col in range(self.size):
            # Extract the column and compress it by removing None values
            compressed_col = [self.arr[row, col] for row in range(self.size) if self.arr[row, col] is not None]
            merged_column = []
            skip = False
            for i in range(len(compressed_col)):
                if skip:
                    skip = False
                    continue
                if i + 1 < len(compressed_col) and compressed_col[i] == compressed_col[i + 1]:
                    merged_column.append(2 * compressed_col[i])
                    self.score += 2 * compressed_col[i]
                    skip = True
                    moved = True
                else:
                    merged_column.append(compressed_col[i])
            # Fill the remaining spaces with None
            merged_column.extend([None] * (self.size - len(merged_column)))
            for row in range(self.size):
                if self.arr[row, col] != merged_column[row]:
                    moved = True
                self.arr[row, col] = merged_column[row]
        if moved:
            self.add_block()

    # Shifts the board down and merges blocks
    def shift_down(self):
        moved = False
        for col in range(self.size):
            # Extract the column and compress it by removing None values
            compressed_col = [self.arr[row, col] for row in range(self.size) if self.arr[row, col] is not None]
            merged_column = []
            skip = False
            for i in range(len(compressed_col) - 1, -1, -1):
                if skip:
                    skip = False
                    continue
                if i - 1 >= 0 and compressed_col[i] == compressed_col[i - 1]:
                    merged_column.insert(0, 2 * compressed_col[i])
                    self.score += 2 * compressed_col[i]
                    skip = True
                    moved = True
                else:
                    merged_column.insert(0, compressed_col[i])
            # Fill the remaining spaces with None
            merged_column = [None] * (self.size - len(merged_column)) + merged_column
            for row in range(self.size):
                if self.arr[row, col] != merged_column[row]:
                    moved = True
                self.arr[row, col] = merged_column[row]
        if moved:
            self.add_block()

    # Shifts the board left and merges blocks
    def shift_left(self):
        moved = False
        for row in range(self.size):
            # Extract the row and compress it by removing None values
            compressed_row = [block for block in self.arr[row] if block is not None]
            merged_row = []
            skip = False
            for i in range(len(compressed_row)):
                if skip:
                    skip = False
                    continue
                if i + 1 < len(compressed_row) and compressed_row[i] == compressed_row[i + 1]:
                    merged_row.append(2 * compressed_row[i])
                    self.score += 2 * compressed_row[i]
                    skip = True
                    moved = True
                else:
                    merged_row.append(compressed_row[i])
            # Fill the remaining spaces with None
            merged_row.extend([None] * (self.size - len(merged_row)))
            for col in range(self.size):
                if self.arr[row, col] != merged_row[col]:
                    moved = True
                self.arr[row, col] = merged_row[col]
        if moved:
            self.add_block()

    # Shifts the board right and merges blocks
    def shift_right(self):
        moved = False
        for row in range(self.size):
            # Extract the row and compress it by removing None values
            compressed_row = [block for block in self.arr[row] if block is not None]
            merged_row = []
            skip = False
            for i in range(len(compressed_row) - 1, -1, -1):
                if skip:
                    skip = False
                    continue
                if i - 1 >= 0 and compressed_row[i] == compressed_row[i - 1]:
                    merged_row.insert(0, 2 * compressed_row[i])
                    self.score += 2 * compressed_row[i]
                    skip = True
                    moved = True
                else:
                    merged_row.insert(0, compressed_row[i])
            # Fill the remaining spaces with None
            merged_row = [None] * (self.size - len(merged_row)) + merged_row
            for col in range(self.size):
                if self.arr[row, col] != merged_row[col]:
                    moved = True
                self.arr[row, col] = merged_row[col]
        if moved:
            self.add_block()

def is_game_over(self):
    # Check for any empty cell
    if np.any(self.arr == None):
        return False
    # Check for possible merges horizontally
    for row in range(self.size):
        for col in range(self.size - 1):
            if self.arr[row, col] == self.arr[row, col + 1]:
                return False
    # Check for possible merges vertically
    for col in range(self.size):
        for row in range(self.size - 1):
            if self.arr[row, col] == self.arr[row + 1, col]:
                return False
    # No empty cells and no possible merges means the game is over
    return True

def interact():
    board = Board()
    while True:
        # Print as a 4x4 grid with tab separation
        for row in board.arr:
            print("\t".join(str(block) if block is not None else "." for block in row))
        print("Score:", board.score)
        if is_game_over(board):
            print("Game Over")
            break
        move = input("Enter move: ")
        if move == "w":
            board.shift_up()
        elif move == "s":
            board.shift_down()
        elif move == "a":
            board.shift_left()
        elif move == "d":
            board.shift_right()
        else:
            print("Invalid move")
            continue

if __name__ == "__main__":
    interact()