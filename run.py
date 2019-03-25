import os, sys

#Create a new project
if sys.argv[1].lower() == "start" or sys.argv[1].lower() == "new" or sys.argv[1].lower() == "project":
	os.system('python new_project.py')

#Create new sequence
if sys.argv[1].lower() == "sequence":
	os.system('python scaffold-sequence.py')