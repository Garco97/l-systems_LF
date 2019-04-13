from tkinter import *
from lsystem_representation import *
import random
import math
LINE_SIZE = 10

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

    def paint_lsystem(self, lsystem, event):
        initial_point = [event.x,event.y]
        direction = "LEFT"
        colour = self.random_colour()
        for letter in lsystem.get_actual_state():
            angle_rads = math.radians(lsystem.angle)
            if letter in lsystem.variables:
                initial_point = (math.cos(angle_rads), math.sin(angle_rads))
                print(initial_point)
                return [i[1] + i[0] * length for i in 
                zip((math.cos(angle_rads), math.sin(angle_rads)),
                    (self._x, self._y))]
                self.create_line(initial_point[0],initial_point[1],initial_point[0]+LINE_SIZE,initial_point[1],width=2, fill=colour)
                # if direction == "RIGHT":
                #     self.create_line(initial_point[0],initial_point[1],initial_point[0]+LINE_SIZE,initial_point[1],width=2, fill=colour)
                #     initial_point=[initial_point[0] + LINE_SIZE, initial_point[1]]
                # elif direction == "LEFT":
                #     self.create_line(initial_point[0],initial_point[1],initial_point[0]-LINE_SIZE,initial_point[1],width=2, fill=colour)
                #     initial_point=[initial_point[0] - LINE_SIZE, initial_point[1]]
                # elif direction == "UP":
                #     self.create_line(initial_point[0],initial_point[1],initial_point[0],initial_point[1] + LINE_SIZE,width=2, fill=colour)
                #     initial_point=[initial_point[0], initial_point[1] + LINE_SIZE]
                # elif direction == "DOWN":
                #     self.create_line(initial_point[0],initial_point[1],initial_point[0],initial_point[1] - LINE_SIZE,width=2, fill=colour)
                #     initial_point=[initial_point[0], initial_point[1] - LINE_SIZE]
            if letter in lsystem.constants:
                if letter == "+":
                    if direction == "RIGHT":
                        lsystem.add_angle(-lsystem.angle)
                        direction = "UP"
                    elif direction == "LEFT":
                        lsystem.add_angle(-lsystem.angle)
                        direction = "DOWN"
                    elif direction == "UP":
                        lsystem.add_angle(-lsystem.angle)
                        direction = "LEFT"
                    elif direction == "DOWN":
                        lsystem.add_angle(-lsystem.angle)
                        direction = "RIGHT"
                elif letter == "-":
                    if direction == "RIGHT":
                        lsystem.add_angle(lsystem.angle)
                        direction = "DOWN"
                    elif direction == "LEFT":
                        lsystem.add_angle(lsystem.angle)
                        direction = "UP"
                    elif direction == "UP":
                        lsystem.add_angle(lsystem.angle)
                        direction = "RIGHT"
                    elif direction == "DOWN":
                        lsystem.add_angle(lsystem.angle)
                        direction = "LEFT"

    def random_colour(self):
        colours = [ "black", "red", "green", "blue", "cyan", "magenta"]
        number = random.randint(0, len(colours)-1)
        return colours[int(number)]