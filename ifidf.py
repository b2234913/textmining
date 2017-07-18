#-*- coding:utf-8 -*-
#import uniout
import csv
import jieba
import sys

from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer


jieba.set_dictionary('dict.txt.big')
corpus = []
form = "json"
with open(form + ".txt", 'r') as f:
	N = []
	for line in f:
		nu = line.split(" ")[0]
		N.append(line.split(" ")[0])
		line = " ".join(line.split(" ")[1:])
		corpus.append(" ".join(jieba.cut(line.split(',')[0], cut_all=False)))
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(corpus)
print tfidf.shape
words = vectorizer.get_feature_names()

with open(form + 'test_data_ifidf.csv','wb') as myfile:
	for i in xrange(len(corpus)):
		a = []
		b = []
		print '----Document %d----' % (i)
		for j in xrange(len(words)):
			if tfidf[i,j] > 1e-5:
				a.append(words[j].encode('utf-8'))
				a.append(tfidf[i,j])
				b.append(a)
				a = []
		b = sorted(b,key=lambda x:x[1],reverse = True)
		b.insert(0,N[i])
		data = []
		for l in range(20): 
			if l ==0:
				print(b[0])
				data.append(b[0])
				continue
			if l < len(b):
				data.append(b[l][0])
				print b[l][0] ,b[l][1]

		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL,lineterminator='\n')
		wr.writerow(data)
