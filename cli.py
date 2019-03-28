import os, time
import generators_helper, console_functions as terminal

#Welcome
terminal.header("Welcome to UiPath Scaffolder!", 'white', 'blue')

#Find installed generators
generators = generators_helper.find_all()

terminal.variable("The following generators are installed: ", generators_helper.to_string())

terminal.input("Please hit any key to choose the generator you wish to use...", allow_empty=True)

#Ask user 
generator = generators[terminal.input_list("Select the framework you would like to use: ", generators)]
terminal.special(generator)

#Run the generator
os.system(generator)