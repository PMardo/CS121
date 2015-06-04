from collections import defaultdict
import math

class Indexer():
	def __init__(self):
		self.__dict = defaultdict(list)

	def BuildIndex(self, tokens, fileName, corpusSize, doc_freq):
		index = open(fileName, 'w')
		for t in tokens:
			t = t.split()
			t2 = t[1].split(":")
			self.__dict[t[0]].append(t2[0]+":"+str(self.__tfidf(t2[1], doc_freq[t[0]], corpusSize)))
		index.write(str(self.__dict))
		index.close()

	def __tfidf(self, termFreq, docFreq, corpusSize):
		termFreq = float(termFreq)
		docFreq = float(docFreq)
		return round(((1 + math.log(termFreq))*math.log((corpusSize/docFreq))), 1)



