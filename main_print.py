from __future__ import print_function
import sys
import traceback
import curses
import life

def main():

   width, height = 80, 10
   iter_max = 50

   def print_draw(universe):
      print("-" * width)
      for y in range(height):
         for x in range(width):
            print("0" if (x, y) in universe.cells else " ", sep='', end='')
         print('')

   simulation = life.Simulation(width, height)
   simulation.run(iter_max, print_draw)

   print(simulation.summary())


# Start the application only if loaded as main
if __name__ == "__main__":
   main()
