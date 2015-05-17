#from Parser import Parser
from Indexer import Indexer
from Reporter import Reporter

indexer = Indexer(["hello.title doc0.3", "world.text doc1.54", "hello.title doc1.2"])
time_taken = indexer.BuildIndex("index.txt")