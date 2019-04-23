from lsystem_representation import *
import json
def get_lsystem(filename):
	'''
	Lee el fichero filename.json
	'''
	with open(filename) as file:
		data = json.load(file)
		system = lsystem(data["rules"], data["axiom"], data["iters"], data["angle"], 3)
		return system