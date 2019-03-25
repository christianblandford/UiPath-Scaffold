#A class for text in the dialog
class Text_Node:
	def __init__(t_type, text, variable=None, color=None)
		self.t_type = t_type #Type of text, can be log/variable/error/warn/header/special/important
		self.text = text #Text that the user will see before responding
		self.variable = variable #variable to print if using a "variable" type text
		self.color = color #color of the text. Can be white/blue/cyan/magenta/yellow/red/grey/green

#A class for questions in the dialog
class Question_Node:
	def __init__(name, text, result_type, q_format, default=None, required=False, answers=None)
		self.name = name #variable to store the response in
		self.text = text #Text that the user will see before responding
		self.result_type = result_type #DataType of the result. Can be string, number, y_n
		self.q_format = q_format #format to ask the question. Can be text or list
		self.default = default #default answer that will be pre-selected for the user
		self.required = required #Is an answer required? True/False
		self.answers = answers #An array of possible answers, if applicable
		self.response # the response from the user

#A class that new generators will use 
class Generator:
	def __init__(name, description, arguments=None, framework_url, default_new_sequence=None, dialog=None, options=None):
		self.name = name #Name of generator
		self.description = description #Description of generator
		self.arguments = arguments #Arguments. Can be project/sequence, etc...
		self.framework_url = framework_url #The URL to the download for the framework
		self.default_new_sequence = default_new_sequence #The sequence that will be copied over
		self.dialog = [];
		self.variables = {};

	#Function to add node to dialog
	def add_dialog_node(node):
		self.dialog.append(node)

	#function to get next dialog node
	def next_dialog():
		if len(self.dialog) > 0:
			return self.dialog.pop(0)

	#Returns dialog node matching given name
	def get_node_by_name(name):
		for item in self.dialog:
			if item.name == name:
				return item

	#Function that will check a given condition and keep/remove dialog node based on this
	def check_node(value_node_name, if_value, dialog_node):
		value = get_node_by_name(value_node_name).response

		if value.lower() != if_value.lower():
			return self.dialog.pop(dialog_node)
