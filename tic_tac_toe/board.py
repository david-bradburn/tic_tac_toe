import numpy as np


class board:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.array = np.zeros((self.height, self.width) , int)
        self.icon = ["    ", "  X ", "  O "]

    def display_terminal(self):
        for x in range(self.height):
            print("-------------------")
            print("|",  end='')
            for y in range(self.width):
                print(self.icon[self.array[x][y]], "|",  end='')
            print("\n", end='')
        print("-------------------")



print("Hello World!!")

test = board()
test.display_terminal()
