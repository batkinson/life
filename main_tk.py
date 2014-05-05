from Tkinter import *
import life

class TkLife(Frame):

   def __init__(self, master=None):
      Frame.__init__(self, master)
      master.resizable(width=FALSE, height=FALSE)
      master.title('Life')
      master.geometry('802x602')
      self.pack(fill=BOTH, expand=YES)
      self.simulation = life.Simulation(80, 60)
      self._create_widgets()
      self.draw()

   def draw(self):
      """Draws the current simulation state."""
      def draw_function(universe):
         cellsize = 10
         self.canvas.delete(ALL)
         for x, y in universe.cells:
            x1 = x * cellsize
            y1 = y * cellsize
            x2 = x1 + cellsize
            y2 = y1 + cellsize
            self.canvas.create_rectangle(x1, y1, x2, y2, fill='gray')

      self.simulation.draw_cells(draw_function)

   def next_state(self):
      """Drives the simulation forward to the next state."""
      self.simulation.next_state()

   def _create_widgets(self):
      """Populates this app with widgets"""
      self.canvas = Canvas(self, width=800, height=600, background='white')
      self.canvas.pack(fill=BOTH, expand=YES)


def main():
   """The main application routine."""
   root = Tk()
   app = TkLife(master=root)

   def simstep():
      app.next_state()
      app.draw()
      root.after(250, simstep)

   root.after(250, simstep)
   app.mainloop()


# Start the application only if loaded as main
if __name__ == "__main__":
   main()
