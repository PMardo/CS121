from Parser import Parser
from Indexer import Indexer
from Reporter import Reporter
import time

corpuspath = "FileDump"
indexfile = "index.txt"
reportfile = "Report.txt"

Parser = Parser()
Indexer = Indexer()
Reporter = Reporter()

t0 = time.clock()
metatuple = Parser.ParseCorpus(corpuspath)
Indexer.BuildIndex(metatuple[2], indexfile, metatuple[0], metatuple[4])
t1 = time.clock()
Reporter.Report(metatuple[0], metatuple[1], indexfile, t1-t0, reportfile)