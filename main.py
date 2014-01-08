import curses
import sys
import traceback
import life

def main():

  try:
    stdscr = curses.initscr()
    scrheight, scrwidth = stdscr.getmaxyx()

    height = scrheight - 2
    width = scrwidth - 2
    
    iterations = None
    
    def cursesdraw(cells):
      stdscr.clear()
      stdscr.border()
      
      # fill cells with universe state
      for y, row in enumerate(cells):
        for x, col in enumerate(row):
          if col:
            stdscr.addch(y+1, x+1, ord('0'))
      stdscr.refresh()
  
    simulation = life.Simulation(width, height)

    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    
    simulation.run(iterations, cursesdraw)

  except KeyboardInterrupt:
    pass
  except:
    curses.endwin()
    print traceback.format_exc()
    sys.exit(1)
  finally:
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    

if __name__ == "__main__":
  main()
