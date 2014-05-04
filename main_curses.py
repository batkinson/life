from __future__ import print_function
import sys
import traceback
import curses
import life

def main():

   std_scr = curses.initscr()
   iter_max = None

   def curses_draw(universe):
      std_scr.erase()
      std_scr.border()
      for x, y in universe.cells:
         std_scr.addch(y+1, x+1, ord('0'))
      std_scr.refresh()

   # Hide cursor
   curses.curs_set(0)

   # Don't echo typed characters to screen
   curses.noecho()

   # Turn off line buffering of input
   curses.cbreak()

   std_scr.nodelay(1)

   try:
      height, width = std_scr.getmaxyx()
      simulation = life.Simulation(width-2, height-2)
      simulation.run(iter_max, curses_draw)
   except KeyboardInterrupt:
      pass
   except:
      curses.endwin()
      print(traceback.format_exc())
      sys.exit(1)
   finally:
      # Return the terminal to a sane state before exiting
      std_scr.nodelay(0)
      curses.nocbreak()
      curses.echo()
      curses.endwin()

   print(simulation.summary())


# Start the application only if loaded as main
if __name__ == "__main__":
   main()
