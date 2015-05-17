from collections import defaultdict
import os
import json
import nltk
## Still Editing this (need to figure out json) - Patrice 
class parser():
    def __init__(self):
        self.__dict = defaultdict(list)
        #self.__corpusPath = corpusPath
        
    def startParse(self, corpusPath):
        folder=os.listdir(corpusPath)
        num_docs = len([d for d in folder if d.endswith('.txt')]) 

        for d in folder:
            if d.endswith('txt'):
                try:
                    file=open(d,'r')
                    print(file)
                finally:
                    file.close()
            else:
                continue
