from Parser import Parser
from Indexer import Indexer
from Reporter import Reporter
import time

Parser = Parser()
Indexer = Indexer()
Reporter = Reporter()

corpuspath = "FileDump"
indexfile = "index.txt"
reportfile = "Report.txt"

t0 = time.clock()
metatuple = Parser.ParseCorpus(corpuspath)
indextime = Indexer.BuildIndex(metatuple[2], indexfile)
t1 = time.clock()
Reporter.Report(metatuple[0], metatuple[1], indexfile, t1-t0, reportfile)