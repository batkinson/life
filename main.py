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

      def curses_draw(cells):
         std_scr.erase()
         std_scr.border()
         for x, y in cells:
            std_scr.addch(y+1, x+1, ord('0'))
         std_scr.refresh()

      curses.curs_set(0)
      curses.noecho()
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
         curses.nocbreak()
         curses.echo()
         curses.endwin()
   else:
      width, height = 80, 10
      iter_max = 50

      def print_draw(cells):
         print("-" * width)
         for y in range(height):
            for x in range(width):
               print("0" if (x, y) in cells else " ", sep='', end='')
            print('')

      simulation = life.Simulation(width, height)
      simulation.run(iter_max, print_draw)

   print(simulation.summary())


# Start the application only if loaded as main
if __name__ == "__main__":
   main()
