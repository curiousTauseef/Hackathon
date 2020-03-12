#https://stackoverflow.com/questions/35857519/efficiently-count-word-frequencies-in-python/35857833
#https://codeburst.io/python-basics-11-word-count-filter-out-punctuation-dictionary-manipulation-and-sorting-lists-3f6c55420855
#Usage : python memEffWayForTopWordsInCorpus.py cleanedPhrasesCorpus_threeDocs.txt
import sys
import io
from collections import Counter

from itertools import dropwhile

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

#infile = '/path/to/input.txt'
infile = sys.argv[1]
#fp = codecs.open(input_file, 'r', 'utf-8')

ngram_vectorizer = CountVectorizer(analyzer='word', ngram_range=(1, 1), min_df=1)

with io.open(infile, 'r', encoding='utf8') as fin:
    X = ngram_vectorizer.fit_transform(fin)
    vocab = ngram_vectorizer.get_feature_names()
    counts = X.sum(axis=0).A1
    freq_distribution = Counter(dict(zip(vocab, counts)))
	#print (freq_distribution.most_common(10))
	#print (freq_distribution.most_common())


#https://stackoverflow.com/questions/15861739/removing-objects-whose-counts-are-less-than-threshold-in-counter
for key, count in dropwhile(lambda key_count: key_count[1] <=1000, freq_distribution.most_common()):
    del freq_distribution[key]


print (freq_distribution.most_common())

