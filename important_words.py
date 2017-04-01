from collections import Counter
from math import log
from sklearn.feature_extraction.text import TfidfVectorizer

def scores(n):

	doc_list = ["script.txt", "transcript_1.txt", "transcript_2.txt", "transcript_3.txt"]
	model = TfidfVectorizer(input = 'filename', ngram_range = (1,3), stop_words = 'english', max_df = 2)

	scores = model.fit_transform(doc_list).toarray()
	feature_names = model.get_feature_names()

	word_scores = zip(scores[0], feature_names)
	word_scores.sort(reverse = True)

	for i in range(n):
		print word_scores[i]