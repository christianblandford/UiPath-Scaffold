
#strips special chars from text to be used when creating a filename
def make_file_name (text) :
	return ''.join(e for e in text if e.isalnum())