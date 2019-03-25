import urllib.request, os, shutil, zipfile, json
from os.path import isfile
from urllib.parse import urlparse

#Creat directory
def create_dir(dir_path):
	os.makedirs(dir_path, 777, True)

def unzip_file(file_path, name=None):
	z_file = zipfile.ZipFile(file_path, 'r')

	#get the name of the output dir from upzip
	output = os.path.join(os.path.dirname(file_path), z_file.namelist()[0])
	#unzip
	z_file.extractall(os.path.dirname(file_path))
	z_file.close()
	#Delete the zip
	os.remove(file_path)
	#name the directory and return
	return rename_dir(output, os.path.join(os.path.dirname(file_path), name))

def update_json_value(key, new_val):
	return None

def read_json_file(file_path) :
	json_file = open(file_path, "r") # Open the JSON file for reading
	data = json.load(json_file) # Read the JSON into the buffer
	json_file.close() # Close the JSON file
	return data

def save_json_file(file_path, new_json):
	json_file = open(file_path, "w+")
	json_file.write(json.dumps(new_json))
	json_file.close()

def rename_dir(src, dst):
	os.rename(src, dst)
	return dst

def download_file(name, url, save_to):
	#determine filetype of download
	path = urllib.parse.urlparse(url).path
	ext = os.path.splitext(path)[1]
	#Create full filename for download
	file_name = name + ext
	file_path = os.path.join(save_to, file_name)

	# Download the file from `url` and save it locally under `file_name`:
	with urllib.request.urlopen(url) as response, open(file_path, 'wb') as out_file:
		shutil.copyfileobj(response, out_file)
		return file_path

def print_dirs(dir_path) :
	for item in os.listdir(dir_path):
    # print path to all subdirectories first.
		if not item in [".screenshots", "Data", "Documentation", "Exceptions_Screenshots"] and not os.path.isfile(item):
			print(" - " + item)

		    # print path to all filenames.
			#for filename in filenames:
			#	print(os.path.join(subdirname, filename))