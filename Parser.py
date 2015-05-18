#     Description (per Ronny's Design.txt)
#         This component parses and tokenizes the corpus into a list of "term.field docId.frequency" tokens, 
#         where stop words are discarded. Once the entire corpus has been tokenized, this list is returned 
#         to the caller. The number of documents and the number of unique words found in the corpus are also 
#         returned to the caller.

# Tips: remember to download NLTK and JSON. 
# What's in my driver.py:
#   import Parser 
#   corpusPath='/Applications/Eclipse /CS121Workspace/Assignment 3/FileDump' <-- add your path to the FileDump
#   p=Parser.parser()
#   p.startParse(corpusPath)

import os, json
from nltk import word_tokenize
from nltk.corpus import stopwords
class parser():
    def __init__(self):
        self.parsed_list=[]
        
    def startParse(self, corpusPath):
        num_docs = len([d for d in os.listdir(corpusPath) if d.endswith('.txt')]) # count docs in corpus, exclude non txt files
        num_unique=0
        finallist=[]
        tempstring=''
        for root, dirs, files in os.walk(corpusPath):
            for file in files:
                if file.endswith(".txt"):
                    data = json.loads(open(os.path.join(root,file)).read())
                    title = data.items()[-1] #does text include title?
                    docid = data.items()[0]
                    text = data.items()[1]
                    tokenized_text = word_tokenize(str(text[1])) #tokenize text str after converting from unicode  
                    words = [w.lower() for w in tokenized_text if not w in stopwords.words('english')]
                    
                    num_unique += len(set(words)) # Num of unique words in entire corpus 
                  
                    freq = {} # Get frequencies
                    for w in words:
                        if freq.has_key(w):
                            freq[w] = freq[w] + 1
                        else:
                            freq[w] = 1
#         Format: "hello.title doc1.2"                   
                else: continue

        return num_docs,num_unique

    


