from __future__ import print_function
import sys
import traceback
import signal
import curses
import atexit
import life


def main(*args):

   std_scr = curses.initscr()
   iter_max = None
   global resizing
   resizing = False

   def resize(*args):
      global resizing
      resizing = True
      curses.endwin()
      std_scr = curses.initscr()
      height, width = std_scr.getmaxyx()
      simulation.universe.resize(width-2, height-2)
   
   def print_summary():
      print(simulation.summary())

   atexit.register(print_summary)

   signal.signal(signal.SIGWINCH,resize)

   def curses_draw(universe):
 
      std_scr.erase()
      std_scr.border()
      for x, y in universe.cells:
         global resizing
         if resizing:
            resizing = False
            break
         std_scr.addch(y+1, x+1, ord('0'))
      std_scr.refresh()

   curses.curs_set(0)
   try:
      height, width = std_scr.getmaxyx()
      simulation = life.Simulation(width-2, height-2)
      simulation.run(iter_max, curses_draw)
   except KeyboardInterrupt:
      pass
   finally:
      curses.curs_set(1)


# Start the application only if loaded as main
if __name__ == "__main__":
   curses.wrapper(main)
