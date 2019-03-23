import urllib.request, os, shutil, zipfile
from urllib.parse import urlparse

#Creat directory
def create_dir(dir_path):
	#stub
	os.makedirs(dir_path)

#Create parent dirs if needed
def create_parent_dirs(dir_path):
	os.makedirs(dir_path + "/../../", 777, True)

def unzip_file(path, name=None):
	print(path)
	z_file = zipfile.ZipFile(path)
	print(z_file)
	z_file.extractall()

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