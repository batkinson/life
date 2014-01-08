from __future__ import print_function
import random
                
class Universe:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[random.choice([True, False, False, False]) for x in xrange(width)] for x in xrange(height)]

    def printgrid(self):
        for row in self.cells:
            for col in row:
                print("*" if col else " ", sep=" ", end="")
            print('')

    def copycells(self):
        self.oldcells = self.cells
        self.cells = [[False for x in xrange(self.width)] for x in xrange(self.height)]
        

    def increment(self):
        self.copycells()
        for rowidx in xrange(self.height):
            for colidx in xrange(self.width):
                self.updatecell(rowidx, colidx)

    def livecell(self, row, col):
        return self.oldcells[row][col]

    def liveneighbors(self, row, col):
        livecount = 0
        height = self.height
        width = self.width
        cells = self.oldcells
        for rowoffset in [-1, 0, 1]:
            for coloffset in [-1, 0, 1]:
                nrow = (row + rowoffset) % height
                ncol = (col + coloffset) % width
                if rowoffset != 0 or coloffset != 0:
                    nlive = self.livecell(nrow, ncol)
                    if nlive:
                        livecount += 1
        return livecount
            
    def updatecell(self, row, col):
        liveneighbors = self.liveneighbors(row, col)
        if self.livecell(row, col):
            self.cells[row][col] = liveneighbors >= 2 and liveneighbors <= 3
        else:
            self.cells[row][col] = liveneighbors == 3


class Simulation:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.universe = Universe(width, height)

    def defaultdraw(cells):
        self.universe.printgrid()
        
    def run(self, max_iter, drawfunc = defaultdraw):
        drawfunc(self.universe.cells)
        if max_iter is None:
            while True:
                self.universe.increment()
                drawfunc(self.universe.cells)
        else:
            for iter in range(1, max_iter + 1):
                self.universe.increment()
                drawfunc(self.universe.cells)
            
