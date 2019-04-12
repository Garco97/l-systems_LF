from point import *
from BresenhamInteger import * 
class lsystem():	
	def __init__(self, variables, constants, rules, initial_state,initial_status,initial_point,size):
		self.point_length = size
		self.variables = variables
		self.constants = constants
		self.rules = rules
		self.initial_state = initial_state
		self.status = initial_status
		self.possible_status = ["U","D","R","L"]
		self.initial_point = initial_point
		self.current_point = self.initial_point

	def rule(self,state):
		state_split = state.split(" ")
		i = 0
		rules = []
		points = []
		for rule in state_split:
			for i in range(0, len(self.variables) ):
				if rule == self.variables[i]:
					rules.append(''.join(self.rules[i][1]) + " ")
					points.append(self.calculate_points())
			for i in range(0, len(self.constants) ):
				if rule == self.constants[i]:
					rules.append(rule[0] + " ")
					self.calculate_status(rule[0])
		rules = ''.join(rules)
		return rules,points

	def calculate_points(self):
		aux = None
		if self.status == "U":
			aux = BresenhamInteger(self.current_point,Point(self.current_point.X,self.current_point.Y - self.point_length))
			self.current_point = Point(self.current_point.X,self.current_point.Y - self.point_length)
		elif self.status == "D":
			aux = BresenhamInteger(self.current_point,Point(self.current_point.X,self.current_point.Y + self.point_length))
			self.current_point = Point(self.current_point.X,self.current_point.Y + self.point_length)
		elif self.status == "R":
			aux = BresenhamInteger(self.current_point,Point(self.current_point.X - self.point_length,self.current_point.Y ))
			self.current_point = Point(self.current_point.X -  self.point_length,self.current_point.Y )
		else:
			aux = BresenhamInteger(self.current_point,Point(self.current_point.X + self.point_length,self.current_point.Y))
			self.current_point = Point(self.current_point.X + self.point_length ,self.current_point.Y )

		return aux

	def calculate_status(self,rule):
		if rule == "+":
			if self.status == "U":
				self.status = "L"

			elif self.status == "D":
				self.status = "R"

			elif self.status == "R":
				self.status = "U"

			else:
				self.status = "D"
		else:
			if self.status == "U":
				self.status = "R"

			elif self.status == "D":
				self.status = "L"

			elif self.status == "R":
				self.status = "D"

			else:
				self.status = "U"



