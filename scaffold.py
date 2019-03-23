#Import statements
import sys, os, time #import libraries
import console_functions as console, text_functions as text, uipath_libraries as frameworks, functions #import modules in this project

#Set up constants
path = os.getcwd()
default_project_dir = "C:\\Users\\chrbla11\\Documents\\UiPath_Projects\\"
#uncomment below for production
#default_project_dir = str(os.path.join(path, p_name))

#Begin

#Welcome
console.header("Welcome to UiPath Scaffolder!", 'blue')

#Get project name
p_name = text.make_file_name(console.input("Please enter a name for your project: "))
console.variable("Project name set to: ", p_name)

#Get Project Description
p_desc = console.input("Project description: ", p_name + " UiPath project.")
console.variable("Project description set to: ", p_desc)

#Get directory
dir_path = console.input("Please enter a path to create your project in: ", os.path.join(default_project_dir, p_name))


#Check if parent dir exists. Error and exit if it does not
if not os.path.isdir(dir_path + "/../../") :
	console.warn("Parent directory does not exist.")
	create_dirs = console.input("Would you like to create the directories now?", "Yes")
	if create_dirs != "Yes":
		console.error("Parent directory does not exist. Please double check and try again.")
		exit(1)
else:
	console.variable("Creating directory:", dir_path)
	functions.create_parent_dirs(dir_path)

	#^^^^^^LOGIC ABOVE NOT WORKING^^^^^^^^^

#Select the framework to use
time.sleep(1) # Sleep one second so user can see output of above input
framework = frameworks.at_index(console.input_list("Select the framework you would like to use: ", frameworks.get_names()))
console.special(framework.name)

zip_file = functions.download_file(p_name, framework.url, dir_path)
functions.unzip_file(os.path.join(zip_file))

console.log(framework.url)

