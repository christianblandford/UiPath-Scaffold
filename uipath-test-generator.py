# A uipath-scaffold generator for UiPath Enhanced REFramework
from generator import Generator, Functions
import uipath



def main():
	enhanced_reframework_generator = Generator(name="Test Generator", description="For showing how the uipath API works.") #Can also define like this: Generator("https://github.com/mihhdu/Enhanced-REFramework/archive/master.zip", "Workblock Snippet\\wbTemplate.xaml")
	
	enhanced_reframework_generator.zip_url = "https://github.com/mihhdu/Enhanced-REFramework/archive/master.zip" # A Zip file to download (the framework)
	enhanced_reframework_generator.default_sequence = "Workblock Snippet\\wbTemplate.xaml" # A default sequence that will be used to create any new sequences

	#Opens a UiPath XAML file for reading and editing
	test_file = uipath.Sequence("OracleEBS Expand NavItem.xaml")

	#argument_to_update.set_direction("in")
	#argument_to_update.set_default_value("Helloooooo Worlddd!!!!")
	#argument_to_update.set_name("in_arg_2")

	#-----------------------------------------------------------------------------------------------------------------------
	#  Get main surrounding block
	#-----------------------------------------------------------------------------------------------------------------------
	def get_main_block():
		print(test_file.get_first_block())


	#-----------------------------------------------------------------------------------------------------------------------
	#  Add argument to main sequence
	#-----------------------------------------------------------------------------------------------------------------------
	def add_arg_to_main_sequence():
		test_file.add_argument("MyArg1", "in", "x:String")
		print(test_file.arguments)
	

	#-----------------------------------------------------------------------------------------------------------------------
	#  Get block by displayname
	#-----------------------------------------------------------------------------------------------------------------------
	def get_block_by_display_name():
		print(test_file.get_node_by_display_name("Assign workblock its name"))

	get_block_by_display_name()
	

	#-----------------------------------------------------------------------------------------------------------------------
	#  List Sequence Variables
	#-----------------------------------------------------------------------------------------------------------------------
	def print_sequence_variables():
		variables = test_file.sequences[0].variables
		for var in variables:
			print(var.type + " " + var.name)

	#-----------------------------------------------------------------------------------------------------------------------
	#  Add Sequence Variables
	#-----------------------------------------------------------------------------------------------------------------------
	def add_sequence_variables():
		print_sequence_variables() #Print before adding
		variables = test_file.sequences[0].create_variable(name="myVar", type="x:String", default="This is my variable.") #Add new variable
		print_sequence_variables() #Print after adding

	#-----------------------------------------------------------------------------------------------------------------------
	#  Delete Sequence Variables
	#-----------------------------------------------------------------------------------------------------------------------
	def delete_sequence_variables():
		print_sequence_variables() #Print before adding
		variables = test_file.sequences[0].delete_variable("myVar") #Add new variable
		print_sequence_variables() #Print after adding

	#-----------------------------------------------------------------------------------------------------------------------
	#  List Invoked Method's Arguments
	#-----------------------------------------------------------------------------------------------------------------------

	def print_invoked_method_args():
		#Start by reading the file
		inner_file = uipath.Sequence(test_file.sequences[0].invoked_workflow_path)
		
		#Print out all of its arguments
		inner_file_args = inner_file.arguments
		for arg in inner_file_args:
			print(str(arg))

	#-----------------------------------------------------------------------------------------------------------------------
	#  Import and print Invoked Method's Arguments
	#-----------------------------------------------------------------------------------------------------------------------
	def import_invoked_method_arguments():
		new_args = test_file.sequences[0].import_arguments()
		for arg in new_args:
			print(arg.key + " " + arg.name + " " + arg.type + " = " + arg.value)

	#-----------------------------------------------------------------------------------------------------------------------
	#  Import and Assign Value to Invoked Method's Arguments
	#-----------------------------------------------------------------------------------------------------------------------
	def set_invoked_method_arg_to_value():
		new_args = test_file.sequences[0].import_arguments()
		new_args[0].set_value("Hello world!")

	#-----------------------------------------------------------------------------------------------------------------------
	#  Import and Assign Variable to Invoked Method's Arguments
	#-----------------------------------------------------------------------------------------------------------------------
	def set_invoked_method_arg_to_variable():
		new_args = test_file.sequences[0].import_arguments()
		new_args[0].set_value("Hello world!")


	#Update arguments of the invoked sequence inside of the main file
	#test_file.sequences[0].invoked_workflow_arguments[0].set_key("in_arg_1")


	#enhanced_reframework_generator.run() # A default method that automatically downloads and unzips a framework (if url is provided)

main()

