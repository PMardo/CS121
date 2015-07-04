Authors:
	Ronald Vega 
	Patrice Mardo 
	Christina Hoang 

Language:
	Python v3.4.3 

Description:
	This Vector Space Search Engine is built to search for documents in the ics.uci.edu domain, which has already already been crawled and stored locally as JSON objects in FileDump

	Indexer.py builds a TF-IDF postings file, Store/index.txt, and collects some statistics, Store/Report.txt

	Query.py is the main module, and uses cosine similarity scoring to retrieve the 5 most relevant documents in the corpus, with respect to a user defined query
