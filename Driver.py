from Parser import Parser
from Indexer import Indexer
from Reporter import Reporter

Parser = Parser()
Indexer = Indexer()
Reporter = Reporter()

corpuspath = "SmallFileDump"
indexfile = "index.txt"
reportfile = "Report.txt"

metatuple = Parser.ParseCorpus(corpuspath)
#print(str(metatuple[2]))
indextime = Indexer.BuildIndex(metatuple[2], indexfile)
Reporter.Report(metatuple[0], metatuple[1], indexfile, indextime, reportfile)
