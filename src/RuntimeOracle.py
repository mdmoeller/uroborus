# Uroboros
# CIS573 Project
# Fall 2012

class RuntimeOracle:

	run = 0
	passed = []
	FILE = ""

	def __init__(self, datafile):
		self.FILE = open(datafile, 'a')

	def getRunNum(self):
		return self.run

	def assertTrue(self, expr, nextRun=True):

		boolResult = bool(expr) # In case we got some other nonsense

		# In case assert has already been called for this run, we 'and' the results
		if len(self.passed) > self.run:
			self.passed[self.run] = self.passed[self.run] and boolResult
		else:
			self.passed.append(boolResult)

		if nextRun:
			self.FILE.write(str(self.run) + '\t' + str(1 if boolResult else 0) + '\n')
			self.run = self.run + 1
