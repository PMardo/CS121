from collections import defaultdict
import time

class Indexer():
	def __init__(self, tokens):
		self.__dict = defaultdict(list)
		self.__tokenList = tokens
	
	def BuildIndex(self, fileName):
		index = open(fileName, 'w')
		self.t0 = time.clock()
		for t in self.__tokenList:
			print("t is " + str(t))
			t = t.split()
			print("t split is " + str(t))
			self.__dict[t[0]].append(t[1])
		index.write(str(self.__dict))
		index.close()
		self.t1 = time.clock()
		return self.t1-self.t0

