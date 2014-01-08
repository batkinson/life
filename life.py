from sets import Set
import random
                
class Universe:

    def __init__(self, width, height):
        self.width, self.height = width, height
        self.cells = Set()
        self.initcells()

    def initcells(self):
        for i in xrange((self.width * self.height) / 4):
            self.cells.add((random.randrange(self.width),random.randrange(self.height)))

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
        width, height = self.width, self.height
        x, y = cell
        for xoffset in [-1, 0, 1]:
            for yoffset in [-1, 0, 1]:
                if not (xoffset == 0 and yoffset == 0):
                    ncell = ((x + xoffset) % width, (y + yoffset) % height)
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
            
