import os

class Reporter():
	def Report(self, a, b, c, d, e):
		self.docs = a
		self.unique = b
		self.index = c
		self.time = d
		self.report = open(e, "w")
		self.report.write("1. There are "+str(self.docs)+" documents in the corpus.\n")
		self.report.write("2. There are "+str(self.unique)+" unique words in the corpus.\n")
		self.report.write("3. The size of the index on disk is "+str(os.path.getsize(self.index)/1000)+"KB\n")
		self.report.write("4. The time taken to build the index was "+str(self.time)+" seconds\n")
		self.report.close()




