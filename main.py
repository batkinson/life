from __future__ import print_function
import curses
import sys
import traceback
import life

def main():

    usecurses = False
    itermax = 15
    width, height = 10, 10
    simulation = life.Simulation(width, height)
    
    if usecurses:
        stdscr = curses.initscr()
	scrheight, scrwidth = stdscr.getmaxyx()
	height, width = scrheight - 2, scrwidth - 2

	def cursesdraw(cells):
            stdscr.erase()
	    stdscr.border()
	    for x, y in cells:
		stdscr.addch(y+1, x+1, ord('0'))    
	    stdscr.refresh()

	curses.curs_set(0)
	curses.noecho()
	curses.cbreak()
	
	try:
	    simulation.run(itermax, cursesdraw)
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
      
	def printdraw(cells):
	    print("-" * width)
	    for x in range(width):
		for y in range(height):
		    print("0" if (x, y) in cells else " ", sep='', end='')
		print('')
	simulation.run(itermax, printdraw)


if __name__ == "__main__":
    main()
