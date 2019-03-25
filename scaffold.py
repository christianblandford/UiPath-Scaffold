#Import statements
import sys, os, time, subprocess, shutil #import libraries
import console_functions as console, text_functions as text, uipath_libraries as frameworks, functions #import modules in this project
from pathlib import Path
from openpyxl import Workbook, load_workbook

#Comment below for production
excel_file_location = "C:\\Users\\chrbla11\\Documents\\Programming\\UiPathScaffolding\\UiPath-Scaffold\\FilesToScaffold.xlsx"

#Create a new object for a sequence. We create these when reading the Excel file.
class Sequence:
	def __init__(self, name, location, parent):
		self.name = name
		self.location = location
		self.parent = parent

#Reads an Excel file for name, location, parent, of items to scaffold
def read_excel(path_to_file):
	console.log("Reading list of sequences from Excel...")
	
	#Load the worksheet as read only
	wb = load_workbook(excel_file_location, read_only=True)
	#Grab the proper worksheet
	ws = wb["Sequences"]

	#Build an array of sequences to scaffold out
	sequences_to_scaffold = []

	#Loop through cells in the worksheet to build the array
	for i,row in enumerate(ws.rows):
		#check if this is the first run of the loop, ignore the data if it is. Due to the excel headers.
		if i > 0:
			name = row[0].value
			location = row[1].value
			parent = row[2].value
			sequences_to_scaffold.append(Sequence(name, location, parent))

	return sequences_to_scaffold

#Get the path to "default" new sequence, for example the wbTemplate from Enhanced ReFramework.
def get_default_sequence(framework):
	default_sequence_path = "";
	if framework.name == "Enhanced ReFramework":
		default_sequence_path = "Workblock Snippet\\wbTemplate.xaml"
	else:
		console.error("Error: no default sequence defined for this framework.")
		exit(1)

	return default_sequence_path


#This method does all the actual work of scaffolding
def scaffold_project(path_to_project, framework):
	console.variable("Scaffolding sequences using ", framework.name)
	time.sleep(1)

	default_sequence_path = os.path.join(path_to_project, get_default_sequence(framework)) #Get the full path to the "default" sequence
	sequences = read_excel(excel_file_location) #get the list of all sequences we want to scaffold out. This comes from the excel file.

	console.log(default_sequence_path)

	for item in sequences:
		#Create parent dirs
		functions.create_dir(os.path.join(path_to_project, item.location))
		shutil.copyfile(default_sequence_path, os.path.join(path_to_project, item.location, item.name + ".xaml")) # Copy the default sequence over to the specified location