from sets import Set
import random
import time

class Universe:

   def __init__(self, width, height):
      self.width, self.height = width, height
      self.cells = Set()
      self._init_cells()

   def next_gen(self):
      """Transform cells to next generation based on the rules of Life."""
      self.neighbors = {}
      self.old_cells = self.cells
      self.cells = Set()
      self._compute_neighbors()
      self._compute_next_gen()

   def _init_cells(self):
      """Seeds the universe with enough life to sustain a number of iterations."""
      for i in xrange((self.width * self.height) / 4):
         self.cells.add((random.randrange(self.width),random.randrange(self.height)))

   def _compute_neighbors(self):
      """For cells neighboring live cells, computes number of live neighbors."""
      for cell in self.old_cells:
         self._mark_neighbors(cell)

   def _mark_neighbors(self, cell):
      """Increment neighbor counts for the given cell's neighbors."""
      width, height = self.width, self.height
      x, y = cell
      for xoff, yoff in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1, 0), (1,1)]:
         nx, ny = (x + xoff) % width, (y + yoff) % height
         if (nx,ny) in self.neighbors:
            self.neighbors[(nx,ny)] += 1
         else:
            self.neighbors[(nx,ny)] = 1

   def _was_live(self, cell):
      """Returns True if the given cell was alive in the prior generation."""
      return cell in self.old_cells

   def _live_neighbors(self, cell):
      """Returns the number of live neighbors for the given cell."""
      return self.neighbors[cell] if cell in self.neighbors else 0

   def _compute_next_gen(self):
      """Populates universe with next generation of cells."""
      for cell in self.neighbors.keys():
         self._procreate(cell)

   def _procreate(self, cell):
      """Adds the given cell to universe, if it should live."""
      liven = self._live_neighbors(cell)
      if liven >= 2 and liven <= 3 and self._was_live(cell):
         self.cells.add(cell)
      elif liven == 3:
         self.cells.add(cell)

class Simulation:

   def __init__(self, width, height):
      self.width, self.height = width, height
      self.universe = Universe(width, height)
      self.ticks = 0
      self.start_time = time.clock()

   def next_state(self):
      self.universe.next_gen()
      self.ticks += 1

   def draw_cells(self, draw_function):
      draw_function(self.universe.cells)

   def _draw_next(self, draw_function):
      self.next_state()
      self.draw_cells(draw_function)

   def run(self, max_iter, draw_func):
      """Runs a simulation for a fixed number of iterations.

         max_iter -- The number of game iterations to run.
         draw_func -- A function to invoke to display the cell grid.
      """

      self.draw_cells(draw_func)

      # The main loop, will loop for max_iter or forever if not specified.
      if max_iter is None:
         while True:
            self._draw_next(draw_func)
      else:
         for iter in xrange(max_iter):
            self._draw_next(draw_func)

   def summary(self):
      """Returns a summary of the simulation."""
      universe = "{0}x{1} cell universe".format(self.width, self.height)
      elapsed_time = time.clock() - self.start_time
      time_per_tick = elapsed_time / self.ticks if self.ticks > 0 else 0
      return "{0} iterations in {1}s ({2}s/iteration), {3}".format(
         self.ticks, elapsed_time, time_per_tick, universe)

