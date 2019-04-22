from tkinter import *
from lsystem_representation import *
import random
import math

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

    def paint_lsystem(self, lsystem, event):
        '''
        Una vez calculadas las iteraciones, se representa el l-system
        '''
        initial_point = [event.x,event.y]
        for letter in lsystem.get_actual_state():
            angle_rad = lsystem.actual_angle * math.pi / 180
            if letter in lsystem.variables:
                destination_point = [initial_point[0] + lsystem.line_size * math.cos(angle_rad) , initial_point[1] + lsystem.line_size * math.sin(angle_rad)]
                self.create_line(initial_point[0],initial_point[1],destination_point[0],destination_point[1],width=2)
                initial_point = destination_point
            if letter == "+":
                lsystem.add_angle(lsystem.angle)
            elif letter == "-":
                lsystem.add_angle(-lsystem.angle)
            elif letter == "[":
                lsystem.stack.append([initial_point,lsystem.actual_angle])
            elif letter == "]":
                initial_point, lsystem.actual_angle = lsystem.stack.pop()


