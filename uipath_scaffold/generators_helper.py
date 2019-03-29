from pkgutil import iter_modules

class generators_helper:
	#find all generators
	@classmethod
	def find_all(cls):
		to_return = []
		for p in iter_modules():
			if "uipath" in p.name and "-generator" in p.name:
				to_return.append(p.name)
		return to_return

	def __str__():
		to_return = ""
		all_items = find_all()

		for i,item in enumerate(all_items):
			if i < len(all_items) - 1:
				to_return = to_return + item + ", "
			else :
				to_return = to_return + item

		return to_return
