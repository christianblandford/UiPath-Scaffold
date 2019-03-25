#Import statements
import sys, os, time, subprocess #import libraries
import console_functions as console, text_functions as text, uipath_libraries as frameworks, functions #import modules in this project
from pathlib import Path

#Set up constants
path = os.getcwd()
default_project_dir = "C:\\Users\\chrbla11\\Documents\\UiPath_Projects\\"
#uncomment below for production
#default_project_dir = str(os.path.join(path, p_name))

#Begin

#Welcome
console.header("Welcome to UiPath Sequence Scaffolder!", 'blue')

#Get directory
dir_path = console.input("Please enter a path to the root of your project: ", default_project_dir)
parent_dir = Path(dir_path).parent

#Open Project directory and read project json
console.log("Checking directory for UiPath project.");
if os.path.isfile(os.path.join(dir_path, "project.json")) :
	p_json = functions.read_json_file(os.path.join(dir_path, "project.json"))
	p_name = p_json["name"]
	p_desc = p_json["description"]
	console.variable("Found project: ", p_name + "(" + p_desc + ")")
else :
	console.error("Error: Could not find project at provided directory.")
	exit(1)

#Print directory tree
console.log("Found these folders in project:")
functions.print_dirs(dir_path)

add_to_dir = console.input("Where would you like to add this sequence?")
console.variable("Okay, adding sequence to: ", add_to_dir)