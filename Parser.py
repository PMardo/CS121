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
        num_docs = len([d for d in os.listdir(corpusPath) if d.endswith('.txt')]) # Count all docs in corpus, exclude non txt files
        num_unique=0
        finallist=[]
        words_in_corpus = []
        for root, dirs, files in os.walk(corpusPath):
            for file in files:
                if file.endswith(".txt"):
                    data = json.loads(open(os.path.join(root,file)).read())
                    items = dict(data.items())
                    text = items['text'] 
                    title = items['title']
                    docid = items['id']

                    tokenized_text = word_tokenize(str(text)) #tokenize text str after converting from unicode  
                    tokenized_title = word_tokenize(str(title))
                    title_words = [w.lower() for w in tokenized_title if not w in stopwords.words('english')]
                    text_words = [w.lower() for w in tokenized_text if not w in stopwords.words('english')]
                    
                    for item in title_words:
                        if item not in words_in_corpus:
                            words_in_corpus.append(item)
                    for item in text_words:
                        if item not in words_in_corpus:
                            words_in_corpus.append(item)
                    
                    freq_text = {} # Get frequencies for each word in each doc
                    freq_title = {}
                    for w in title_words:
                        if w in freq_title:
                            freq_title[w] = freq_title[w] + 1
                        else:
                            freq_title[w] = 1
                    for w in text_words:
                        if w in freq_text:
                            freq_text[w] = freq_text[w] + 1
                        else:
                            freq_text[w] = 1
                    
                    for k,v in freq_text.items(): # take the freq dict keys and values, add it to a temp string for formatting, then add that string to a permanent list
                        # string should look like: term.field docID.frequency
                        textstring = k+'.'+'text'+' doc'+str(int(docid))+'.'+str(v) # Note docid is actually a float, converted it to int. But we may want to keep it as a float...         
                        finallist.append(textstring)  
                    for k,v in freq_title.items(): # take the freq dict keys and values, add it to a temp string for formatting, then add that string to a permanent list
                        # string should look like: term.field docID.frequency
                        titlestring = k+'.'+'title'+' doc'+str(int(docid))+'.'+str(v) # Note docid is actually a float, converted it to int. But we may want to keep it as a float...         
                        finallist.append(titlestring)

        num_unique = len(words_in_corpus) # Num of unique words in entire corpus 
        a = (num_docs, num_unique, finallist)
        return a
