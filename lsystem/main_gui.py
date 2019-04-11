from tkinter import *
from resizable_canvas import *
class Main_GUI:
	def __init__(self):
		self.root = Tk()
		self.root.geometry("800x600")
		self.frame = Frame(width=100000, height=150)
		self.frame.pack(side=TOP , expand=False)
		self.mycanvas = ResizingCanvas(self.root,width=200, height=10000)
		self.mycanvas.pack(side=BOTTOM, expand=False)
		self.mycanvas.configure(background='black')
		self.initial_state_lbl = Label(self.frame, text="Estado inicial")
		self.initial_state_lbl.pack(side=LEFT)
		self.initial_state_lbl.place(relx=0.001, rely=0.2)
		self.initial_state = Entry(self.frame, width=5)
		self.initial_state.pack(side=LEFT)
		self.initial_state.place(relx=0.115, rely=0.2)
		self.iterations_lbl = Label(self.frame, text="Iteraciones")
		self.iterations_lbl.pack(side=LEFT)
		self.iterations_lbl.place(relx=0.19, rely=0.2)
		self.iterations = Entry(self.frame,width=2)
		self.iterations.pack(side=LEFT)
		self.iterations.place(relx=0.285, rely=0.2)
		self.button_rules = Button(self.frame,text="Guardar regla", command=self.save_rule)
		self.button_rules.pack(side=LEFT)
		self.button_rules.place(relx=0.9, rely=0.2)
		self.variables_lbl = Label(self.frame, text="Variables")
		self.variables_lbl.pack(side=LEFT)
		self.variables_lbl.place(relx=0.9, rely=0.2)
		self.variables = Entry(self.frame)
		self.variables.pack(side=LEFT)
		self.variables.place(relx=0.9, rely=0.1)
		self.constants_lbl = Label(self.frame, text="Constantes")
		self.constants_lbl.pack(side=LEFT)
		self.constants_lbl.place(relx=0.9, rely=0.1)
		self.constants = Entry(self.frame)
		self.constants.pack(side=LEFT)
		self.constants.place(relx=0.9, rely=0.1)
		self.rules_lbl = Label(self.frame, text="Reglas")
		self.rules_lbl.pack(side=LEFT)
		self.rules_lbl.place(relx=0.9, rely=0.1)
		self.rules = Entry(self.frame)
		self.rules.pack(side=LEFT)
		self.rules.place(relx=0.9, rely=0.1)
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