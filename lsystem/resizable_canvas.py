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
		'''
		Reescala el canvas cuando la pantalla se hace más grande o más pequeña
		'''
		wscale = float(event.width)/self.width
		hscale = float(event.height)/self.height         
		self.width = event.width
		self.height = event.height
		self.parent.initial_point = [self.width/2, self.height/2]
		self.config(width=self.width, height=self.height)

	


