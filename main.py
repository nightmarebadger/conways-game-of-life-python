from numpy import array
from time import sleep


class GameOfLife(object):
    def __init__(self, n, starting=[]):
        self.game = array([[0]*n]*n)
        self.size = n
        for i, j in starting:
            self.game[i, j] = 1

    def get_square_pos(self, i, j):
        im = i - 1
        iM = i + 2

        jm = j - 1
        jM = j + 2

        if im < 0:
            im = 0
        if jm < 0:
            jm = 0

        return ((im, iM), (jm, jM))

    def get_rule(self, i, j):
        x, y = self.get_square_pos(i, j)

        rule_n = self.game[x[0]:x[1], y[0]:y[1]].sum()

        alive = self.game[i, j] == 1

        # If currently alive
        if alive:
            rule_n -= 1
            # Any live cell with fewer than two live neighbours dies, as if
            # caused by under-population.
            if rule_n < 2:
                return 0
            # Any live cell with two or three live neighbours lives on to the
            # next generation.
            elif rule_n < 4:
                return 1
            # Any live cell with more than three live neighbours dies, as if by
            # overcrowding.
            else:
                return 0
        # If currently dead
        else:
            # Any dead cell with exactly three live neighbours becomes a live
            # cell, as if by reproduction.
            if rule_n == 3:
                return 1
            else:
                return 0

    def step(self):
        self.game_new = self.game.copy()

        for j in range(self.size):
            for i in range(self.size):
                self.game_new[i, j] = self.get_rule(i, j)

        self.game = self.game_new

    def play(self):
        count = 0
        while(True):
            print("Step", count)
            self.draw()
            self.step()
            count += 1
            sleep(1)

    def draw(self):
        drawing = ""
        for j in range(self.size):
            for i in range(self.size):
                if self.game[i, j]:
                    drawing += "X"
                else:
                    drawing += " "
            drawing += "\n"
        drawing += "\n"
        print(drawing)
