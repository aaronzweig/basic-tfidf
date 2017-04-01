from math import log
from sklearn.feature_extraction.text import TfidfVectorizer
import os

def scores(n):

	doc_list = ["script.txt"]

	for file in os.listdir("."):
	    if file.endswith(".txt"):
	        name = os.path.basename(file)
	        if name != "script.txt":
	        	doc_list.append(name)

	model = TfidfVectorizer(input = 'filename', ngram_range = (1,3), stop_words = 'english', max_df = 2)

	scores = model.fit_transform(doc_list).toarray()
	feature_names = model.get_feature_names()

	word_scores = zip(scores[0], feature_names)
	word_scores.sort(reverse = True)

	for i in range(n):
		print word_scores[i]