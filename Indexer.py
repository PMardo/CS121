from Parser import Parser
from Reporter import Reporter
import time
from collections import defaultdict
import math

class Indexer():
	def __init__(self):
		self.__dict = defaultdict(list)
		self.__docMags = {}

	def BuildIndex(self, tokens, fileName, corpusSize, doc_freq):
		index = open(fileName, 'w')
		for t in tokens:
			t = t.split()
			t2 = t[1].split(":")
			self.tfidf = self.__tfidf(t2[1], doc_freq[t[0]], corpusSize)
			self.__dict[t[0]].append(t2[0]+":"+str(self.tfidf))
		index.write(str(dict(self.__dict)))
		index.close()

	def __tfidf(self, termFreq, docFreq, corpusSize):
		termFreq = float(termFreq)
		docFreq = float(docFreq)
		return round(((1 + math.log(termFreq))*math.log((corpusSize/docFreq))), 1)

corpuspath = "FileDump"
indexfile = "Store/index.txt"
reportfile = "Store/Report.txt"

Parser = Parser()
Indexer = Indexer()
Reporter = Reporter()

t0 = time.clock()
metatuple = Parser.ParseCorpus(corpuspath)
Indexer.BuildIndex(metatuple[2], indexfile, metatuple[0], metatuple[4])
t1 = time.clock()
Reporter.Report(metatuple[0], metatuple[1], indexfile, t1-t0, reportfile)


