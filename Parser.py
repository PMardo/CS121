from collections import defaultdict
import os, json, nltk
#     Description
#         This component parses and tokenizes the corpus into a list of "term.field docId.frequency" tokens, 
#         where stop words are discarded. Once the entire corpus has been tokenized, this list is returned 
#         to the caller. The number of documents and the number of unique words found in the corpus are also 
#         returned to the caller.

# What's in my driver.py:
# import Parser 
# corpusPath='/Applications/Eclipse /CS121Workspace/Assignment 3/FileDump' <-- add your path to the FileDump
# p=Parser.parser()
# p.startParse(corpusPath)

class parser():
    def __init__(self):
        self.parsed_list=[] # Still need to work on adding to this list...
    def startParse(self, corpusPath):
        num_docs = len([d for d in os.listdir(corpusPath) if d.endswith('.txt')]) 
        s=''
        for root, dirs, files in os.walk(corpusPath):
            for file in files:
                if file.endswith(".txt"):
                    data = json.loads(open(os.path.join(root,file)).read())
                    docid = data.items()[0]
                    text = data.items()[1]
                    title = data.items()[-1]      
                else: continue
        return num_docs
