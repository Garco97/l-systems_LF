from tkinter import filedialog
from tkinter import *
from resizable_canvas import *
from lsystem_representation import *
from read_JSON import *
class Main_GUI:
	def __init__(self):
		self.rules = {}
		self.rule_counter = 0.1
		self.create_GUI()
		
	def save_rule(self):
		'''
		Guarda la regla que esté escrita en ese momento en los campos de variable y regla
		'''
		variable = str(self.variables_entry.get())
		rule = str(self.rules_entry.get())
		if len(variable) == 1:
			self.rules[variable]=rule
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
		actual_lsystem  = lsystem(self.rules, self.initial_state_entry.get(),
									   self.iterations_entry.get(),float(self.angulo_entry.get()),int(self.line_size_entry.get()),self.actual_angle)
		for iteration in range(0,int(actual_lsystem.iterations)):
			actual_lsystem.calculate()
		self.mycanvas.paint_lsystem(actual_lsystem,event)

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
				text = Label(self.mycanvas, text=variable+":"+rule,bg="white")
				text.pack(side=LEFT)
				text.place(relx=0.85, rely=self.rule_counter)
				self.rule_counter += 0.03
			self.rules=lsystem.rules
			self.actual_angle = lsystem.actual_angle
			angle = StringVar()
			iterations = StringVar()
			initial = StringVar()
			angle.set(lsystem.angle) 
			iterations.set(lsystem.iterations)
			initial.set(lsystem.initial_state)
			self.refresh_GUI(angle, iterations, initial)

	def refresh_GUI(self, angle, iterations, initial):
		'''
		Función que refresca los datos de la interfaz cuando cargas un fichero JSON
		'''
		self.angulo_entry = Entry(self.frame, textvariable=angle)
		self.angulo_entry.pack(side=LEFT)
		self.angulo_entry.place(relx=0.735, rely=0.3)
		self.iterations_entry = Entry(self.frame, textvariable=iterations)
		self.iterations_entry.pack(side=LEFT)
		self.iterations_entry.place(relx=0.735, rely=0.1)
		self.initial_state_entry = Entry(self.frame, textvariable=initial)
		self.initial_state_entry.pack(side=LEFT)
		self.initial_state_entry.place(relx=0.13, rely=0.1)

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
		self.mycanvas = ResizingCanvas(self.root,width=200, height=400)
		self.mycanvas.pack(side=BOTTOM, expand=False)
		self.mycanvas.configure(background='white')
		self.initial_state_lbl = Label(self.frame, text="Estado inicial")
		self.initial_state_lbl.pack(side=LEFT)
		self.initial_state_lbl.place(relx=0.001, rely=0.1)
		self.initial_state_entry = Entry(self.frame)
		self.initial_state_entry.pack(side=LEFT)
		self.initial_state_entry.place(relx=0.13, rely=0.1)
		self.iterations_lbl = Label(self.frame, text="Iteraciones")
		self.iterations_lbl.pack(side=LEFT)
		self.iterations_lbl.place(relx=0.62, rely=0.1)
		self.iterations_entry = Entry(self.frame)
		self.iterations_entry.pack(side=LEFT)
		self.iterations_entry.place(relx=0.735, rely=0.1)
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
		self.angulo_lbl = Label(self.frame, text="Angulo")
		self.angulo_lbl.pack(side=LEFT)
		self.angulo_lbl.place(relx=0.62, rely=0.3)
		self.angulo_entry = Entry(self.frame)
		self.angulo_entry.pack(side=LEFT)
		self.angulo_entry.place(relx=0.735, rely=0.3)
		size = StringVar()
		size.set("2")
		self.line_size_lbl = Label(self.frame, text="Tam. Linea")
		self.line_size_lbl.pack(side=LEFT)
		self.line_size_lbl.place(relx=0.62, rely=0.5)
		self.line_size_entry = Entry(self.frame, textvariable=size)
		self.line_size_entry.pack(side=LEFT)
		self.line_size_entry.place(relx=0.735, rely=0.5)
		self.mycanvas.addtag_all("all")
		self.mycanvas.bind("<Button-1>", self.calculate)	
		self.root.mainloop()

if __name__ == '__main__':
	Main_GUI()