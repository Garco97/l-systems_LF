from tkinter import filedialog
from tkinter import *
from resizable_canvas import *
from lsystem_representation import *
from read_JSON import *
class Main_GUI:
	def __init__(self):
		self.rules = {}
		self.rule_counter = 0.1
		self.actual_angle = 90
		self.initial_point = None
		self.create_GUI()
		
	def save_rule(self):
		'''
		Guarda la regla que esté escrita en ese momento en los campos de variable y regla
		'''
		variable = str(self.variables_entry.get())
		rule = str(self.rules_entry.get())
		if len(variable) == 1:self.rule_representation(variable, rule)
			

	def rule_representation(self, variable, rule):
		'''
		Representa la regla en el canvas
		'''
		self.rules[variable]={'rule':rule,'forward':self.check.get()}
		self.variables_entry.delete(0, len(variable))
		self.rules_entry.delete(0,len(rule))
		text = Label(self.mycanvas, text=variable+":"+rule,bg="white")
		text.pack(side=LEFT)
		text.place(relx=0.85, rely=self.rule_counter)
		self.rule_counter += 0.03

	def calculate(self,event):
		'''
		 Se encarga de guardar el lsystem creado para poder representarlo despues
		'''
		self.mycanvas.delete("all")
		self.initial_point=[event.x,event.y]
		self.actual_angle = int(self.popupMenuVar.get())
		if self.is_not_empty():
			actual_lsystem  = lsystem(self.rules, self.initial_state_entry.get(),
										   self.iterations_entry.get(),float(self.angle_entry.get()),int(self.line_size_entry.get()),self.actual_angle)
			for iteration in range(0,int(actual_lsystem.iterations)):
				actual_lsystem.calculate()
			self.mycanvas.paint_lsystem(actual_lsystem,event)

	def repaint(self,event):
		'''
		Pinta de nuevo el l-system cargado con las actualizaciones de los entry
		'''
		if self.initial_point is not  None and event.char == "\r":
			event.x,event.y = self.initial_point[0], self.initial_point[1]
			self.calculate(event)

	def is_not_empty(self):
		'''
		Comprueba si hay algún campo vacio
		'''
		if self.initial_state_entry.get() is  "" or self.iterations_entry.get() is "" or self.angle_entry.get() is "" or self.line_size_entry.get() is "":
			return False
		else:return True

	def lsystem_json(self):
		'''
		Carga el fichero JSON desde un filechooser
		'''
		self.rules = {}
		self.rule_counter = 0.1
		self.root.filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))
		if self.root.filename is not "": 
			lsystem = get_lsystem(self.root.filename)
			for variable, rule in lsystem.rules.items():
				self.rule_representation(variable, rule["rule"])
			self.rules=lsystem.rules
			self.actual_angle = lsystem.actual_angle
			self.angle.set(lsystem.angle) 
			self.iterations.set(lsystem.iterations)
			self.initial.set(lsystem.initial_state)
			self.popupMenuVar.set(str(self.actual_angle)) 

	def create_GUI(self):
		'''
		Crea toda la interfaz gráfica
		'''
		self.root = Tk()
		self.root.geometry("1000x750")
		self.frame = Frame(width=600, height=150)
		self.frame.pack(side=TOP , expand=False)
		self.button_load_JSON = Button(self.root,text="Cargar JSON", command = self.lsystem_json)
		self.button_load_JSON.pack(side=LEFT)
		self.button_load_JSON.place(relx=0.1, rely=0.05)
		self.popupMenuVar = StringVar(self.root)
		choices = { '0','90','180','270'}
		self.popupMenuVar.set('0') 
		self.popupMenu = OptionMenu(self.root, self.popupMenuVar, *choices)
		self.popupMenu.place(relx=0.1, rely=0.08)
		self.popUpMenu_lbl = Label(self.root, text="Orientación")
		self.popUpMenu_lbl.pack(side=LEFT)
		self.popUpMenu_lbl.place(relx=0.04, rely=0.08)
		self.check = IntVar()
		self.chechButton = Checkbutton(self.root, text="Avance", variable=self.check)
		self.chechButton.pack(side=TOP)
		self.chechButton.place(relx=0.49, rely=0.06)
		self.mycanvas = ResizingCanvas(self.root,width=200, height=400)
		self.mycanvas.pack(side=BOTTOM, expand=False)
		self.mycanvas.configure(background='white')
		self.initial = StringVar()
		self.initial_state_lbl = Label(self.frame, text="Estado inicial")
		self.initial_state_lbl.pack(side=LEFT)
		self.initial_state_lbl.place(relx=0.001, rely=0.1)
		self.initial_state_entry = Entry(self.frame,textvariable=self.initial)
		self.initial_state_entry.pack(side=LEFT)
		self.initial_state_entry.place(relx=0.13, rely=0.1)
		self.initial_state_entry.bind("<Key>", self.repaint)

		self.iterations_lbl = Label(self.frame, text="Iteraciones")
		self.iterations_lbl.pack(side=LEFT)
		self.iterations_lbl.place(relx=0.62, rely=0.1)
		self.angle = StringVar()
		self.iterations = StringVar()
		self.iterations.set("2")
		self.iterations_entry = Entry(self.frame,textvariable=self.iterations)
		self.iterations_entry.pack(side=LEFT)
		self.iterations_entry.place(relx=0.735, rely=0.1)
		self.iterations_entry.bind("<Key>", self.repaint)
		self.button_rules = Button(self.frame,text="Guardar regla", command=self.save_rule)
		self.button_rules.pack(side=LEFT)
		self.button_rules.place(relx=0.4, rely=0.75)
		self.variables_lbl = Label(self.frame, text="Variables")
		self.variables_lbl.pack(side=LEFT)
		self.variables_lbl.place(relx=0.001, rely=0.3)
		self.variables_entry = Entry(self.frame)
		self.variables_entry.pack(side=LEFT)
		self.variables_entry.place(relx=0.13, rely=0.3)
		self.rules_lbl = Label(self.frame, text="Reglas")
		self.rules_lbl.pack(side=LEFT)
		self.rules_lbl.place(relx=0.001, rely=0.5)
		self.rules_entry = Entry(self.frame)
		self.rules_entry.pack(side=LEFT)
		self.rules_entry.place(relx=0.13, rely=0.5)
		self.angle_lbl = Label(self.frame, text="Angulo")
		self.angle_lbl.pack(side=LEFT)
		self.angle_lbl.place(relx=0.62, rely=0.3)
		self.angle_entry = Entry(self.frame,textvariable=self.angle)
		self.angle_entry.pack(side=LEFT)
		self.angle_entry.place(relx=0.735, rely=0.3)
		self.angle_entry.bind("<Key>", self.repaint)
		size = StringVar()
		size.set("4")
		self.line_size_lbl = Label(self.frame, text="Tam. Linea")
		self.line_size_lbl.pack(side=LEFT)
		self.line_size_lbl.place(relx=0.62, rely=0.5)
		self.line_size_entry = Entry(self.frame, textvariable=size)
		self.line_size_entry.pack(side=LEFT)
		self.line_size_entry.place(relx=0.735, rely=0.5)
		self.line_size_entry.bind("<Key>", self.repaint)
		self.mycanvas.addtag_all("all")
		self.mycanvas.bind("<Button-1>", self.calculate)	
		self.root.mainloop()

if __name__ == '__main__':
	Main_GUI()