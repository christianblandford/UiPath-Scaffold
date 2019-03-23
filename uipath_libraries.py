from Framework import Framework # import framework object so we can create them

all_frameworks = []

reframework = Framework("ReFramework", "https://github.com/UiPath/ReFrameWork/archive/master.zip")
all_frameworks.append(reframework)
enhanced_reframework = Framework("Enhanced ReFramework", "https://github.com/mihhdu/Enhanced-REFramework/archive/master.zip")
all_frameworks.append(enhanced_reframework)



#Returns a list of all framework objects
def get() :
	return all_frameworks

#Returns a framework at an index
def at_index(num):
	return all_frameworks[num]

#Returns a list of strings of all framework names
def get_names():
	to_return = []
	for item in all_frameworks:
		to_return.append(item.name)
	return to_return

#returns a string of all available frameworks
def as_string():
	to_return = ""
	for index,item in enumerate(all_frameworks):
		if index == len(all_frameworks) - 1:
			to_return = to_return + item.name
		else:
			to_return = to_return + item.name + ", "

	return to_return