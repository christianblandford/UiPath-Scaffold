import os
import subprocess
import console_functions as terminal
from .generators_helper import *

#Welcome
terminal.header("Welcome to UiPath Scaffolder!", 'white', 'blue')

#Find installed generators
generators =  generators_helper.find_all()

if len(generators) == 0:
	terminal.error("No generators have been installed. Please install one and try again.")
	exit(1)
else:
	terminal.variable("The following generators are installed: ", str(generators))

	terminal.input("Type any key to choose the generator you wish to use...", allow_empty=True)

	#Ask user 
	generator = generators[terminal.input_list("Select the framework you would like to use: ", generators)]
	terminal.special(generator)

	#Run the generator
	subprocess.run(generator)