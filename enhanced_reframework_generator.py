import uipath_generator as Generator

#Define variables to create generator with
name = "Enhanced REFramework"
description = "A UiPath Studio template upon which you can build, test and run attended and unattended business processes, irrespective of process data types and process linearity."
arguments = ["Sequence", "Project"]
framework_url = "https://github.com/mihhdu/Enhanced-REFramework/archive/master.zip"
default_new_sequence = "Workblock Snippet\\wbTemplate.xaml"

#Create the generator
enhanced_reframework_generator = Generator(name, description, arguments=None, framework_url, default_new_sequence=None, dialog=None, options=None)

#Create the dialog nodes as needed.
Generator.add_dialog_node(Generator.Text_Node("header", "Welcome to the Enhanced-REFramework Generator!"))
Generator.add_dialog_node(Generator.Question_Node("scaffold_sequences", "Would you like to scaffold out project directories and sequences?", "y_n", "text", "Y"))
Generator.add_dialog_node(Generator.Text_Node("log", "Okay, I will scaffold out a project for you.")) #Add text node saying okay
#enhanced_reframework_generator.check_node("scaffold_sequences", "y", 2) #Remove the text node that says okay if the user selected anything besides "y" (case insenitive)