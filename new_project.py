#Import statements
import sys, os, time, subprocess #import libraries
import console_functions as console, text_functions as text, uipath_libraries as frameworks, functions, scaffold #import modules in this project
from pathlib import Path

#Set up constants
path = os.getcwd()
default_project_dir = os.path.join(os.path.expanduser("~\\Documents"), "UiPath_Projects")
#uncomment below for production
#default_project_dir = str(os.path.join(path, p_name))

#Begin

#Welcome
console.header("Welcome to UiPath Scaffolder!", 'blue')

#Get project name
p_name = text.make_project_name(console.input("Please enter a name for your project: ")) #Prompts user for project name and formats the input appropriately
console.variable("Project name set to: ", p_name)

#Get Project Description
p_desc = console.input("Project description: ", p_name + " UiPath project.")
console.variable("Project description set to: ", p_desc)

#Get directory
dir_path = console.input("Please enter a path to create your project in: ", os.path.join(default_project_dir, p_name))
parent_dir = Path(dir_path).parent

#Check if parent dir exists. Error and exit if it does not
if not os.path.isdir(parent_dir) :
	console.warn("Parent directory does not exist.")
	create_dirs = console.input("Would you like to create the directories now?", "Y")
	if create_dirs != "Y":
		console.error("Parent directory does not exist. Please double check and try again.")
		exit(1)

#Create directories
console.variable("Creating parent directory: ", parent_dir)
functions.create_dir(parent_dir)

#Select the framework to use
time.sleep(1) # Sleep one second so user can see output of above input
framework = frameworks.at_index(console.input_list("Select the framework you would like to use: ", frameworks.get_names()))
console.variable("Using: ", framework.name)
console.variable("Downloading framework from: ", framework.url)

#Download framework .zip
zip_file = functions.download_file(p_name, framework.url, parent_dir)
#unzipping file
console.variable("Unpacking file: ", zip_file)
new_file = functions.unzip_file(zip_file, p_name)
console.header("Project " + p_name + " successfully created at " + new_file + "!", 'yellow')

#Update the project.json
console.log("Updating project.json with project information.")
p_json_path = os.path.join(new_file, "project.json") # save path to project.json
p_json = functions.read_json_file(p_json_path) # read JSON file
p_json["name"] = p_name 
p_json["description"] = p_desc
functions.save_json_file(p_json_path, p_json) # save JSON file
console.log("Done.");

#ask if user wants to scaffold out sequences
scaffold_project = console.input("Would you like to scaffold out project directories and sequences?", "Y")
if scaffold_project is not "Y":
	console.log("Okay, you can always return to this step later. Opening project in Explorer...")
	time.sleep(2)
	subprocess.call("explorer " + dir_path, shell=True)
	exit(0)
else:
	console.log("Okay, I will scaffold out a project for you.")

	#Call the method to actually do the scaffolding
	scaffold.scaffold_project(dir_path, framework)

	console.header("Scaffolding successully complete for project  " + p_name + "!", 'green')

	if console.input("Would you like me to open the project for you now?", "Y"):
		subprocess.call("explorer " + dir_path, shell=True)
	else:
		console.input("Okay. Your project has been created at: " + dir_path + ". Exiting now.")
	exit(0)