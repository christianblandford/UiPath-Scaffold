# UiPath-Scaffold

Scaffolds out UiPath projects using one of the selected Frameworks. 
Generates project.json with project name and description. 
Adds sequences as needed.


To create a new generator, just create a new .py file with uipath-XXXXX-generator.py as the file name. This file must create a new instance of Generator. The GeneratorAPI in cli.py will pick it up and use it.

# Usage
* python cli.py
  * Scaffolds a new project after allowing you to choose the generator you would like.
  * *Note:* you must install a generator before this program will do anything