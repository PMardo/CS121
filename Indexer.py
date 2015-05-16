import time

class Indexer():
	def __init__(self, tokens):
		self.dictionary = {} 
		self.tokenList = tokens
	
	def BuildIndex():
		postingsFile = open("index.txt", 'w')
		t0 = time.clock()
		for t in self.tokenList:
			postingsList = []
			t.split()
			if dictionary.has_key(t[0]):
				print ("hello")
