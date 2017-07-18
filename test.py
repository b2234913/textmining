#-*- coding:utf-8 -*-
import uniout
import jieba
import sys

from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = []
with open("json_1_1.txt", 'r') as f:
    for line in f:
        corpus.append(" ".join(jieba.cut(line.split(',')[0], cut_all=False)))

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(corpus)
print tfidf.shape
words = vectorizer.get_feature_names()
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
    
    
    id = b[0]
    b = sorted(b[1:],key=lambda x:x[1],reverse = True)
    b.insert(0,id)
    #print len(b)
    print(b)

    for l in range(20): 
        if l < len(b):
            print b[l][0] ,b[l][1]
            #print(b)
    
