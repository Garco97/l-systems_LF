from tkinter import *
from lsystem_representation import *
import random
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()
        self.parent = parent

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height 
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

    def paint_lsystem(self, lsystem):
        initial_point = [self.width/2,self.height/2]
        direction = "LEFT"
        colour = self.random_colour()

        for letter in lsystem.get_actual_state():
            if letter in lsystem.variables:
                if direction == "RIGHT":
                    self.create_line(initial_point[0],initial_point[1],initial_point[0]+20,initial_point[1],width=3, fill=colour)
                    initial_point=[initial_point[0]+20,initial_point[1]]
                elif direction == "LEFT":
                    self.create_line(initial_point[0],initial_point[1],initial_point[0]-20,initial_point[1],width=3, fill=colour)
                    initial_point=[initial_point[0]-20,initial_point[1]]
                elif direction == "UP":
                    self.create_line(initial_point[0],initial_point[1],initial_point[0],initial_point[1] + 20,width=3, fill=colour)
                    initial_point=[initial_point[0],initial_point[1] + 20]
                elif direction == "DOWN":
                    self.create_line(initial_point[0],initial_point[1],initial_point[0],initial_point[1] - 20,width=3, fill=colour)
                    initial_point=[initial_point[0],initial_point[1] - 20]
            if letter in lsystem.constants:
                if letter == "+":
                    if direction == "RIGHT":
                        direction = "UP"
                    elif direction == "LEFT":
                        direction = "DOWN"
                    elif direction == "UP":
                        direction = "LEFT"
                    elif direction == "DOWN":
                        direction = "RIGHT"
                elif letter == "-":
                    if direction == "RIGHT":
                        direction = "DOWN"
                    elif direction == "LEFT":
                        direction = "UP"
                    elif direction == "UP":
                        direction = "RIGHT"
                    elif direction == "DOWN":
                        direction = "LEFT"
    def random_colour(self):
        colours = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
        number = random.randint(0, len(colours)-1)
        return colours[int(number)]