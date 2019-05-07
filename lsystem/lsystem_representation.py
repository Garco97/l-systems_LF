class lsystem():
	def __init__(self, rules, initial_state, iterations, angle, line_size, starting_angle):
		self.rules = rules
		self.variables = set([])
		self.initial_state = initial_state
		self.iterations = iterations
		self.actual_state = initial_state
		self.angle = angle % 360
		self.actual_angle = starting_angle
		self.line_size = line_size
		self.forward_variables = set([])
		self.stack = []
		self.take_variables()
		self.take_forward_variables()

	def __str__(self):
		res = "El lsystem tiene las siguientes reglas\n"
		res += str(self.rules) +"\n"
		return res

	def take_forward_variables(self):
		'''
		Extrae las variables que hacen que se pinte de las reglas
		'''
		for i,j in self.rules.items():
			if j["forward"] == 1:
				self.forward_variables.add(i)
	def take_variables(self):
		'''
		Extrae las variables de las reglas
		'''
		for i,j in self.rules.items():
			self.variables.add(i)

	def add_angle(self, angle):
		'''
		Añade el angulo pasado como parametro y hace mod 360 del angulo actual
		'''
		self.actual_angle += angle
		self.actual_angle = self.actual_angle % 360

	def calculate(self):
		'''
		Calcula el siguiente estado del l-sistema en función del estado actual
		'''
		next_state = ""
		found = False
		for variable in self.actual_state:
			for var, rule in self.rules.items():
				if variable == var:
					next_state += rule["rule"]
					found = True
					break
			if not found:
				next_state += variable
			found = False
		self.set_actual_state(next_state)

	def set_actual_state(self,actual_state):
		'''
		Establece el estado actual
		'''
		self.actual_state = actual_state

	def get_actual_state(self):
		'''
		Retorna el estado actual
		'''
		return self.actual_state