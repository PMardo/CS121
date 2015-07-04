import os, json
from nltk import word_tokenize
from nltk.corpus import stopwords

class Parser():
    def ParseCorpus(self, corpusPath):
        corpus_size = len([d for d in os.listdir(corpusPath) if d.endswith('.txt')])
        doc_freq = {}
        doc_url = {}
        finallist=[]
        term_space = []
        for root, dirs, files in os.walk(corpusPath):
            for file in files:
                if file.endswith(".txt"):
                    data = json.loads(open(os.path.join(root,file)).read())
                    items = dict(data.items())                    
                    text = items['text'] 
                    docid = items['id']
                    url = items['_id']

                    doc_url["doc"+str(int(docid))] = url

                    tokenized_text = word_tokenize(str(text.encode('utf-8')))
                    text_words = [w.lower() for w in tokenized_text if not w in stopwords.words('english')]
                    
                    for item in text_words:
                        if item not in term_space:
                            term_space.append(item)
                    
                    freq_text = {}
                    for w in text_words:
                        if w in freq_text:
                            freq_text[w] = freq_text[w] + 1
                        else:
                            freq_text[w] = 1
                            if w in doc_freq:
                                doc_freq[w] = doc_freq[w] + 1
                            else:
                                doc_freq[w] = 1
                
                    for k,v in freq_text.items():
                        # string should look like: term docID:frequency
                        textstring = k+' doc'+str(int(docid))+':'+str(v)
                        finallist.append(textstring)  
        with open("Store/termspace.txt", "w") as f:
            f.write(str(term_space))
        with open("Store/docfrequencies.txt", "w") as g:
            g.write(str(doc_freq))
        with open("Store/docurls.txt", "w") as h:
            h.write(str(doc_url))
        a = (corpus_size, len(term_space), finallist, term_space, doc_freq)
        return a
