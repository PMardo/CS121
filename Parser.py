#     Description (per Ronny's Design.txt)
#         This component parses and tokenizes the corpus into a list of "term.field docId.frequency" tokens, 
#         where stop words are discarded. Once the entire corpus has been tokenized, this list is returned 
#         to the caller. The number of documents and the number of unique words found in the corpus are also 
#         returned to the caller.

# Tips: remember to download NLTK and JSON. Also, use a smaller file to run code -- see SmallFileDump folder
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
        self.parsed_list=[] # didn't use this yet-- idk if i need it. 
        
    def startParse(self, corpusPath):
        num_docs = len([d for d in os.listdir(corpusPath) if d.endswith('.txt')]) # Count all docs in corpus, exclude non txt files
        num_unique=0
        finallist=[]
        tempstring=''
        for root, dirs, files in os.walk(corpusPath):
            for file in files:
                if file.endswith(".txt"):
                    data = json.loads(open(os.path.join(root,file)).read())
                    title = data.items()[-1] # ******* NEED TO INCLUDE TITLES ************
                    docid = data.items()[0]
                    text = data.items()[1]
                    
                    tokenized_text = word_tokenize(str(text[1])) #tokenize text str after converting from unicode  
                    words = [w.lower() for w in tokenized_text if not w in stopwords.words('english')] #  ***** REMOVE NUMBERS W REGEX *****
                   
                    num_unique += len(set(words)) # Num of unique words in entire corpus 
                    
                    freq = {} # Get frequencies for each word in each doc
                    for w in words:
                        if freq.has_key(w):
                            freq[w] = freq[w] + 1
                        else:
                            freq[w] = 1
                    
                    for k,v in freq.items(): # take the freq dict keys and values, add it to a temp string for formatting, then add that string to a permanent list
                        # string should look like: term.field docID.frequency
                        tempstring = k+'.'+str(text[0])+' doc'+str(int(docid[1]))+'.'+str(v) ; # Note docid is actually a float, converted it to int. But we may want to keep it as a float... 
                        finallist.append(tempstring)
                    print(finallist)                 
                else: continue
        return num_docs,num_unique,finallist
