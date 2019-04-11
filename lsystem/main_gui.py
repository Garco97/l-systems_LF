from tkinter import *
from resizable_canvas import *
class Main_GUI:
	def __init__(self):
		self.root = Tk()
		self.root.geometry("800x600")
		self.mycanvas = ResizingCanvas(self.root, bg='white',width=2, height=2)
		self.mycanvas.pack()
		self.mycanvas.configure(background='lightgray')
		self.initial_state_lbl = Label(self.root, text="Estado inicial")
		self.initial_state_lbl.pack(side=BOTTOM)
		self.initial_state = Entry(self.root)
		self.initial_state.pack(side=BOTTOM)
		self.iterations_lbl = Label(self.root, text="Iteraciones")
		self.iterations_lbl.pack(side=BOTTOM)
		self.iterations = Entry(self.root)
		self.iterations.pack(side=BOTTOM)
		self.button_rules = Button(self.root,text="Guardar regla", command=self.save_rule)
		self.button_rules.pack(side=BOTTOM)
		

		self.variables_lbl = Label(self.root, text="Variables")
		self.variables_lbl.pack(side=LEFT)
		self.variables = Entry(self.root)
		self.variables.pack(side=LEFT)
		self.constants_lbl = Label(self.root, text="Constantes")
		self.constants_lbl.pack(side=LEFT)
		self.constants = Entry(self.root)
		self.constants.pack(side=LEFT)
		self.rules_lbl = Label(self.root, text="Reglas")
		self.rules_lbl.pack(side=LEFT)
		self.rules = Entry(self.root)
		self.rules.pack(side=LEFT)
		self.mycanvas.addtag_all("all")

		#self.mycanvas.bind("<Button-1>", self.paint)
		self.root.mainloop()

	def save_rule(self):
		print("test")
		pass
	# def paint(self,event):
	# 	variables = self.variables.get().split()

	# 	constants = self.mycanvasonstants.get().split()
	# 	count = 0
	# 	for i in self.rules.get():
	# 		if i == "/":
	# 			count = count + 1
	# 	rules = []
	# 	aux = self.rules.get()
	# 	if count != 0 :
	# 		for i  in range(0,count + 1):
	# 			aux = aux.split("/",1)
	# 			rule = aux[0]
	# 			if len(aux) > 1:
	# 				aux = aux[1]
	# 			rules.append(rule.split(","))
	# 	else:
	# 		rules.append(aux.split(","))
	# 	initial_state = self.initial_state.get()
	# 	iterations = int(self.iterations.get())

	# 	aux = lsystem(variables,constants,rules,initial_state,'R',Point(event.x,event.y),2)
	# 	self.paint_lsystem(aux,iterations)
	# def paint_lsystem(self, lsystem, iterations):
	# 	self.mycanvas.delete("all")
	# 	self.mycanvas.configure(background='gray')

	# 	rules, points = lsystem.rule(lsystem.initial_state)
	# 	for i in range(0,iterations - 1):
	# 		rules, points = lsystem.rule(rules)

	# 	for elemento in points:
	# 		for el in elemento:
	# 			self.mycanvas.create_oval(el.X,el.Y,el.X,el.Y)
		


if __name__ == '__main__':
    Main_GUI()