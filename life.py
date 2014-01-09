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

    def nexttick(self):
        self.neighbors = {}
        self.oldcells = self.cells
        self.cells = Set()
        self.computeneighbors()
        self.computenextgen()

    def computeneighbors(self):
        for cell in self.oldcells:
            self.markneighbors(cell)

    def markneighbors(self, cell):
        width, height = self.width, self.height
        x, y = cell
        for xoff, yoff in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1, 0), (1,1)]:
            nx, ny = (x + xoff) % width, (y + yoff) % height
            if (nx,ny) in self.neighbors:
                self.neighbors[(nx,ny)] += 1
            else:
                self.neighbors[(nx,ny)] = 1

    def waslive(self, cell):
        return cell in self.oldcells
    
    def liveneighbors(self, cell):
        return self.neighbors[cell] if cell in self.neighbors else 0
    
    def computenextgen(self):
        for cell in self.neighbors.keys():
            self.procreate(cell)

    def procreate(self, cell):
        liven = self.liveneighbors(cell)
        if liven >= 2 and liven <= 3 and self.waslive(cell):
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
            self.universe.nexttick()

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
            
