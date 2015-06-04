#     Description (per Ronny's Design.txt)
#         This component parses and tokenizes the corpus into a list of "term.field docId.frequency" tokens, 
#         where stop words are discarded. Once the entire corpus has been tokenized, this list is returned 
#         to the caller. The number of documents and the number of unique words found in the corpus are also 
#         returned to the caller.

import os, json
from nltk import word_tokenize
from nltk.corpus import stopwords

class Parser():
    def ParseCorpus(self, corpusPath):
        corpus_size = len([d for d in os.listdir(corpusPath) if d.endswith('.txt')]) # Count all docs in corpus, exclude non txt files
        doc_freq = {}
        finallist=[]
        term_space = []
        for root, dirs, files in os.walk(corpusPath):
            for file in files:
                if file.endswith(".txt"):
                    data = json.loads(open(os.path.join(root,file)).read())
                    items = dict(data.items())
                    text = items['text'] 
                    docid = items['id']

                    tokenized_text = word_tokenize(str(text.encode('utf-8')))
                    text_words = [w.lower() for w in tokenized_text if not w in stopwords.words('english')]
                    
                    for item in text_words:
                        if item not in term_space:
                            term_space.append(item)
                    
                    freq_text = {} # Get frequencies for each word in each doc               
                    for w in text_words:
                        if w in freq_text:
                            freq_text[w] = freq_text[w] + 1
                        else:
                            freq_text[w] = 1
                            if w in doc_freq:
                                doc_freq[w] = doc_freq[w] + 1
                            else:
                                doc_freq[w] = 1
                    
                    for k,v in freq_text.items(): # take the freq dict keys and values, add it to a temp string for formatting, then add that string to a permanent list
                        # string should look like: term docID:frequency
                        textstring = k+' doc'+str(int(docid))+':'+str(v) # Note docid is actually a float, converted it to int. But we may want to keep it as a float...         
                        finallist.append(textstring)  

        a = (corpus_size, len(term_space), finallist, term_space, doc_freq)
        return a
