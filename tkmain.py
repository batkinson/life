from Tkinter import *
import life

class TkLife(Frame):
      
   def __init__(self, master=None):
      Frame.__init__(self, master)
      master.resizable(width=FALSE, height=FALSE)
      master.title('Life')
      master.geometry('805x605')
      self.pack()
      self.simulation = life.Simulation(80, 60)
      self.createWidgets()
      self.draw()

   def createWidgets(self):
      self.canvas = Canvas(self, width=800, height=600, background='white')
      self.canvas.pack()

   def draw(self):
      cells = self.simulation.universe.cells
      cellsize = 10
      self.canvas.delete(ALL)
      for x, y in cells:
         x1 = x * cellsize
         y1 = y * cellsize
         x2 = x1 + cellsize
         y2 = y1 + cellsize
         self.canvas.create_rectangle(x1, y1, x2, y2, fill='gray')

   def nextstate(self):
      self.simulation.universe.nexttick()

root = Tk()

app = TkLife(master=root)

def simstep():
   app.nextstate()
   app.draw()
   root.after(250, simstep)

root.after(250, simstep)
app.mainloop()


