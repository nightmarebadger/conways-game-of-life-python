from __future__ import division

from numpy import array
from pyglet.window import key

import pyglet


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

    def clear(self):
        self.game = array([[0]*self.size]*self.size)

# A blinker, which moves between two positions:
#
# XXX
#
# and
#
#  X
#  X
#  X
#
blinker = [(0, 1), (1, 1), (2, 1)]

# A toad, which moves between two positions:
#
#  XXX
# XXX
#
# and
#
#   X
# X  X
# X  X
#  X
#
toad = [(0, 2), (1, 2), (2, 2),
        (1, 1), (2, 1), (3, 1)]

# A beacon, which moves between two positions:
#
# XX
# XX
#   XX
#   XX
#
# and
#
# XX
# X
#    X
#   XX
#
beacon = [(0, 0), (0, 1), (1, 0), (1, 1),
          (2, 2), (2, 6), (3, 2), (3, 3)]

glider = [(2, 0), (0, 1), (2, 1), (1, 2), (2, 2)]
diehard = [(11, 19), (15, 19), (16, 19), (17, 19), (10, 20), (11, 20),
           (16, 21)]

lwss = [(1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (4, 2), (4, 3), (0, 4), (3, 4)]
random1 = [(18, 16), (19, 16), (20, 16), (21, 16), (16, 17), (17, 17),
           (22, 17), (23, 17), (15, 18), (24, 18), (14, 19), (25, 19),
           (13, 20), (16, 20), (18, 20), (20, 20), (22, 20), (26, 20),
           (13, 21), (15, 21), (17, 21), (19, 21), (21, 21), (23, 21),
           (26, 21), (13, 22), (26, 22), (13, 23), (26, 23), (13, 24),
           (19, 24), (20, 24), (26, 24), (13, 25), (26, 25), (13, 26),
           (19, 26), (20, 26), (26, 26), (13, 27), (26, 27), (13, 28),
           (16, 28), (17, 28), (18, 28), (21, 28), (22, 28), (23, 28),
           (26, 28), (13, 29), (16, 29), (18, 29), (21, 29), (23, 29),
           (26, 29), (13, 30), (16, 30), (17, 30), (18, 30), (21, 30),
           (22, 30), (23, 30), (26, 30), (13, 31), (26, 31), (13, 32),
           (26, 32), (14, 33), (25, 33), (15, 34), (24, 34), (16, 35),
           (17, 35), (22, 35), (23, 35), (18, 36), (19, 36), (20, 36),
           (21, 36)]


game_window = pyglet.window.Window(
    width=800,
    height=800,
    caption="Conway's Game of Life"
)

pyglet.gl.glClearColor(1, 1, 1, 1)

n = 50

game = GameOfLife(n, random1)

width = game_window.width
height = game_window.height
w = width // game.size
h = height // game.size


@game_window.event
def on_draw():
    game_window.clear()
    for i in range(1, n):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ('v2i', (i*w, 0,
                     i*w, height)),
            ('c3B', (0, 0, 0,
                     0, 0, 0))
        )

        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ('v2i', (0, i*h,
                     width, i*h)),
            ('c3B', (0, 0, 0,
                     0, 0, 0))
        )

    for j in range(game.size):
        for i in range(game.size):
            if game.game[i, j] == 1:
                pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                    [0, 1, 2, 0, 2, 3],
                    ('v2i', (i*w, j*h,
                             (i+1)*w-1, j*h,
                             (i+1)*w-1, (j+1)*h-1,
                             i*w, (j+1)*h-1)),
                    ('c3B', (100, 100, 100,
                             100, 100, 100,
                             100, 100, 100,
                             100, 100, 100))
                )


@game_window.event
def on_key_press(symbol, modifiers):
    global running
    # Step
    if symbol == key.RIGHT:
        game.step()
    # Run/pause
    if symbol == key.SPACE:
        if running:
            pyglet.clock.unschedule(update)
            running = False
        else:
            pyglet.clock.schedule_interval(update, 1/5)
            running = True
    # Clear
    if symbol == key.C:
        game.clear()
    # "Record" (print current values)
    if symbol == key.R:
        tmp = []
        for j in range(game.size):
            for i in range(game.size):
                if game.game[i, j] == 1:
                    tmp.append((i, j))
        print(tmp)


@game_window.event
def on_mouse_press(x, y, button, modifiers):
    global w, h
    i = x // w
    j = y // h
    if game.game[i, j] == 1:
        game.game[i, j] = 0
    else:
        game.game[i, j] = 1


def update(dt):
    game.step()


if __name__ == '__main__':
    running = False
    pyglet.app.run()
