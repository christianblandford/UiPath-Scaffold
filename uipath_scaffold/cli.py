import os
import subprocess
import console_functions as console
from .generators_helper import *

#Welcome
console.header("Welcome to UiPath Scaffolder!", 'white', 'blue')

#Find installed generators
generators =  generators_helper.find_all()

if len(generators) == 0:
	console.error("No generators have been installed. Please install one and try again.")
	exit(1)
else:
	print(generators)
	console.variable("The following generators are installed: ", str(generators))

	console.input("Type any key to choose the generator you wish to use...", allow_empty=True)

	#Ask user 
	generator = generators[console.input_list("Select the framework you would like to use: ", generators)]
	console.special(generator)

	#Run the generator
	os.system("python -m " + generator)

