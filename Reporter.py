import os

class Reporter():
	def __init__(self, a, b, c, d):
		self.docs = a
		self.unique = b
		self.index = c
		self.time = d

	def Report(self):
		report = open("Report.txt", "w")
		report.write("1. There are %d documents in the corpus.\n",self.docs)
		report.write("2. There are %d unique words in the corpus.\n",self.unique)
		report.write("3. The size of the index on disk is %dKB\n",os.path.getsize(index)/1000)
		report.write("4. The time taken to build the index was %d seconds\n",self.time)
		report.close()




