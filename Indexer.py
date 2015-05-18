from collections import defaultdict
import time

class Indexer():
	def __init__(self):
		self.__dict = defaultdict(list)
	
	def BuildIndex(self, tokens, fileName):
		self.__tokenList = tokens
		index = open(fileName, 'w')
		self.t0 = time.clock()
		for t in self.__tokenList:
			t = t.split()
			self.__dict[t[0]].append(t[1])
		index.write(str(str(self.__dict).encode('utf-8')))
		index.close()
		self.t1 = time.clock()
		return self.t1-self.t0

