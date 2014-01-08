from sets import Set
import random
                
class Universe:

    def __init__(self, width, height):
        self.width, self.height = width, height
        self.cells = Set()
        self.initcells()

    def initcells(self):
        random.seed()
        for i in xrange((self.width * self.height) / 4):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            self.cells.add((x,y))

    def copycells(self):
        self.oldcells = self.cells
        self.cells = Set()        

    def increment(self):
        self.copycells()
        for x in range(self.width):
            for y in range(self.height):
                self.updatecell((x, y))

    def livecell(self, cell):
        return cell in self.oldcells

    def liveneighbors(self, cell):
        livecount = 0
        height, width = self.height, self.width
        row, col = cell
        for rowoffset in [-1, 0, 1]:
            for coloffset in [-1, 0, 1]:
                if not (rowoffset == 0 and coloffset == 0):
                    ncell = ((row + rowoffset) % height, (col + coloffset) % width)
                    if self.livecell(ncell):
                        livecount += 1
        return livecount
            
    def updatecell(self, cell):
        liven = self.liveneighbors(cell)
        if self.livecell(cell):
            if liven >= 2 and liven <= 3:
                self.cells.add(cell)
        elif liven == 3:
            self.cells.add(cell)


class Simulation:

    def __init__(self, width, height):
        self.width, self.height = width, height
        self.universe = Universe(width, height)
        
    def run(self, max_iter, drawfunc):

        def drawcells():
            drawfunc(self.universe.cells)

        def nextstate():
            self.universe.increment()

        def drawnext():
            nextstate()
            drawcells()

        drawcells()
        
        if max_iter is None:
            while True:
                drawnext()
        else:
            for iter in xrange(max_iter):
                drawnext()
            
