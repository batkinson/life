from __future__ import print_function
import curses
import sys
import traceback
import life

def main():

   use_curses = True

   if use_curses:
      std_scr = curses.initscr()
      scr_height, scr_width = std_scr.getmaxyx()
      height, width = scr_height - 2, scr_width - 2
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

      try:
         simulation = life.Simulation(width, height)
         simulation.run(iter_max, curses_draw)
      except KeyboardInterrupt:
         pass
      except:
         curses.endwin()
         print(traceback.format_exc())
         sys.exit(1)
      finally:
         # Return the terminal to a sane state before exiting
         curses.nocbreak()
         curses.echo()
         curses.endwin()
   else:
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
