import numpy as np


class board:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.array = np.zeros((self.height, self.width) , int)
        self.icon = ["    ", "  X ", "  O "]
        self.state = 1
        self.win_state = 0

    def display_terminal(self):
        for x in range(self.height):
            print("-------------------")
            print("|",  end='')
            for y in range(self.width):
                print(self.icon[self.array[x][y]], "|",  end='')
            print("\n", end='')
        print("-------------------")

    def check_win(self, state):

        for x in range(self.width):
            count = 0
            for y in range(self.height):
                if self.array[x][y] == state:
                    count += 1

            if count == 3:
                print("Congratulations player {}! You have won!".format(self.icon[state]))
                self.win_state = 1
                return

        for y in range(self.height):
            count = 0
            for x in range(self.width):
                if self.array[x][y] == state:
                    count += 1

            if count == 3:
                print("Congratulations player {}! You have won!".format(self.icon[state]))
                self.win_state = 1
                return


        count = 0
        for x in range(self.width):
            if self.array[x][x] == state:
                count += 1

        if count == 3:
            print("Congratulations player {}! You have won!".format(self.icon[state]))
            self.win_state = 1
            return


        count = 0
        for x in range(self.width):
            if self.array[x][self.width - 1 - x] == state:
                count += 1

        if count == 3:
            print("Congratulations player {}! You have won!".format(self.icon[state]))
            self.win_state = 1
            return
        return

    def place(self, x, y, symbol):

        if type(x) != int or type(y) != int:
            print("Please enter an integer")
            return

        elif x > self.width or y > self.height:
            print("Please enter a number in range")
            return

        if int(self.array[x - 1][y - 1]) != 0:
            print("There is already a {} there you cannot place a {} on this spot \n Please choose a different spot\n"
                  .format(self.icon[self.array[x - 1][y - 1]], self.icon[symbol]))
            return

        else:
            self.array[x - 1][y - 1] = symbol

            board.check_win(self, symbol)

            if self.win_state != 1:
                if self.state == 1:
                    self.state = 2
                else:
                    self.state = 1
            return

    def input_icon(self):
        try:
            x = int(input("Player {}, please select a horizontal coordinate between 1 and {} inclusive"
                          .format(self.icon[self.state], self.width)))
        except:
            print("Please enter an integer")
            return

        try:
            y = int(input("Player {}, please select a vertical coordinate between 1 and {} inclusive"
                          .format(self.icon[self.state], self.width)))
        except:
            print("Please enter an integer")
            return

        board.place(self, x, y, self.state)
        return

    def main(self):

        board.display_terminal(self)

        while self.win_state != 1 :

            board.input_icon(self)
            board.display_terminal(self)


print("Hello World!!")

game = board()
game.main()