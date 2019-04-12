class lsystem():
	def __init__(self, constants, rules, initial_state, iterations):
		self.constants = constants
		self.rules = rules
		self.variables = set([])
		self.initial_state = initial_state
		self.iterations = iterations
		self.actual_state = initial_state
		self.degree = 90
		self.take_variables()

	def take_variables(self):
		for i,j in self.rules.items():
			self.variables.add(i)

	def __str__(self):

		res = "El lsystem tiene las siguientes constantes\n"
		res += str(self.constants) +"\n"
		res += "Las siguientes reglas:\n"
		res += str(self.rules) +"\n"
		return res
	def calculate(self):
		next_state = ""
		found = False
		for variable in self.actual_state:
			for var, rule in self.rules.items():
				if variable == var:
					next_state += rule
					found = True
					break
			if not found:
				next_state += variable
			found = False

		self.set_actual_state(next_state)
	def set_actual_state(self,actual_state):
		self.actual_state = actual_state
	def get_actual_state(self):
		return self.actual_state