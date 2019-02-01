class World:
	pits = {}

	def __init__(self):
		print("World has been created")


	def addPit(self, pCoord, pKey):
		result = False

		if not self.pits.has_key(pKey):
			self.pits[pKey] = pCoord
			result = True

		return result


