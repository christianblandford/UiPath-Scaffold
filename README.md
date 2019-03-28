# UiPath-Scaffold

Scaffolds out UiPath projects using one of the selected Frameworks. 
Generates project.json with project name and description. 
Adds sequences as needed.

UiPath API in uipath.py allows a programmer to interact with UiPath XAML files with ease(sorta).

To create a new generator, just create a new .py file with uipath-XXXXX-generator.py as the file name. This file must create a new instance of Generator. The GeneratorAPI in cli.py will pick it up and use it.

# Dependencies
This app has a few dependencies that you must install by running the following commands first:
pip install termcolor
pip install pick
pip install windows-curses
pip install opnpyxl
pip install beautifulsoup4
pip install lxml

# Usage
* python cli.py
  * Scaffolds a new project after allowing you to choose the generator you would like. 