# Conway's Game of Life - Python

Trying to answer the "How would you implement [Conway's Game of
Life](http://en.wikipedia.org/wiki/Conway's_Game_of_Life) in Python" question.

It's just a quick and dirty job, but it should work well for smaller fields
(it's set to 50x50 so you can actually see something, feel free to change/play
with it to see how far it goes :) ). I've added some starting positions in the
code for you to choose from. Apart from that, you can manually set everything
up:

| Binding                  | Command                                            |
| -----------              | -------------------------------------------------- |
| Mouse click (on a field) | Change the value of field (dead/alive)             |
| Right arrow              | Go one step forward                                |
| Space                    | Start/pause "animation" (5 steps per second)       |
| C                        | Clear the board                                    |
| R                        | Record the current live fields (prints to console) |




# Rules

The universe of the Game of Life is an infinite two-dimensional orthogonal grid
of square cells, each of which is in one of two possible states, alive or dead.
Every cell interacts with its eight neighbours, which are the cells that are
horizontally, vertically, or diagonally adjacent. At each step in time, the
following transitions occur:

1. Any live cell with fewer than two live neighbours dies, as if caused by
   under-population.
2. Any live cell with two or three live neighbours lives on to the next
   generation.
3. Any live cell with more than three live neighbours dies, as if by
   overcrowding.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if
   by reproduction.

The initial pattern constitutes the seed of the system. The first generation is
created by applying the above rules simultaneously to every cell in the
seed—births and deaths occur simultaneously, and the discrete moment at which
this happens is sometimes called a tick (in other words, each generation is a
pure function of the preceding one). The rules continue to be applied
repeatedly to create further generations.
