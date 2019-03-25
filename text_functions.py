
#strips special chars from text to be used when creating a filename
def make_file_name (text) :
	return ''.join(e for e in text if e.isalnum())

#Converts to Title Case
def make_title_case(text) :
	return text.title()

#Creates a string that is suitable for a UiPath Project Name
def make_project_name(text):
	return make_file_name(make_title_case(text))