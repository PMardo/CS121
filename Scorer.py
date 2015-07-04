from collections import defaultdict, OrderedDict
import os, ast, math

class Scorer():
	def __init__(self):
		self.corpus_size = len([d for d in os.listdir("FileDump") if d.endswith('.txt')])
		self.term_space = []
		self.index = {}
		self.docMags = {}
		self.doc_freqs = {}
		self.doc_urls = {}
		with open("Store/index.txt", "r") as f:
			self.dict = f.read()
			self.index.update(ast.literal_eval(self.dict))
		with open("Store/termspace.txt", "r") as g:
			self.terms = g.read()
			self.term_space.extend(ast.literal_eval(self.terms))
		with open("Store/docfrequencies.txt", "r") as h:
			self.freqs = h.read()
			self.doc_freqs.update(ast.literal_eval(self.freqs))		
		with open("Store/docurls.txt", "r") as i:
			self.urls = i.read()
			self.doc_urls.update(ast.literal_eval(self.urls))

	def Calc_Doc_Mags(self):
		with open("Store/docMags.txt", "w") as docVectorMags:
			for term in self.term_space:		
				for item in self.index[term]:
					docId_freq = item.split(":")
					if docId_freq[0] in self.docMags:
						self.docMags[docId_freq[0]] += math.pow(float(docId_freq[1]), 2)
					else:
						self.docMags[docId_freq[0]] = math.pow(float(docId_freq[1]), 2)
			for k,v in self.docMags.items():
				self.docMags[k] = math.sqrt(v)
			docVectorMags.write(str(self.docMags))

	def Get_RelevancyList(self, query):
		query_list = query.split();
		query_tfs = {}
		sim_scores = {}
		
		for term in query_list:
			if term in self.term_space:
				if term in query_tfs:
					query_tfs[term] += 1
				else:
					query_tfs[term] = 1
			else:
				if term not in query_tfs:
					query_tfs[term] = float(0)
		
		for t,f in query_tfs.items():
			if f != 0.0:
				query_tfs[t] = self.__tfidf(f, self.doc_freqs[t])
		
		query_mag = self.__Calc_Query_Mag(query_tfs)

		for t,f in query_tfs.items():
			if t in self.term_space:
				for token in self.index[t]:
					token = token.split(":")
					if token[0] in sim_scores:
						sim_scores[token[0]] += float(f*float(token[1]))
					else:
						sim_scores[token[0]] = float(f*float(token[1]))
			
		for d,f in sim_scores.items():
			sim_scores[d] = sim_scores[d] / (query_mag*self.docMags[d])

		top5docs = []
		sorted_by_value = OrderedDict(sorted(sim_scores.items(), key=lambda x: x[1], reverse=True))
		i = 0
		url_list = []
		for k,v in sorted_by_value.items():
			if (i == 5):
				return url_list
			else:
				url_list.append(self.doc_urls[k])
				i += 1

	def __tfidf(self, termFreq, docFreq):
		termFreq = float(termFreq)
		docFreq = float(docFreq)
		return round(((1 + math.log(termFreq))*math.log((self.corpus_size/docFreq))), 1)
	
	def __Calc_Query_Mag(self, query_tfs):
		squaresum = 0	
		for t,f in query_tfs.items():
			if f != 0.0:
				squaresum += math.pow(float(f), 2)
		return math.sqrt(squaresum)

"""
queries = ["mondego","machine learning","software engineering","security","student affairs","graduate courses","informatics","REST","computer games","information retrieval"]
score = Scorer()
score.Calc_Doc_Mags()
with open("Storage/query_hits.txt", "w") as q:
	for query in queries:
		top_urls = []
		top_urls = score.Get_RelevancyList(query)
		if top_urls is not None:
			q.write("Top Results for: "+query+"\n")
			i = 1
			for url in top_urls:				
				q.write(str(i)+". "+url+"\n")
				i += 1
			q.write("\n")			
		else:
			q.write("No Results for: "+query+"\n\n")
"""