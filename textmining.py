#coding:utf8
import re
import io
import sys
import os
import csv
import codecs
import gensim
import jieba
from gensim.models import word2vec

def main():
	f = open('xml_1.csv','rb')
	x = []
	with codecs.open("seg_xml_text.txt",'w','utf-8') as fz:
		for row in csv.reader(f):
			unicode_row = [x.decode('utf8') for x in row]
		#print(unicode_row[1])
			seg_list = jieba.cut(unicode_row[1], cut_all=False)
			x = ' '.join(seg_list)
			string = re.sub("[\s+\.\!\/_,$%^*()+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), " ".decode("utf8"),x)	
			print(string)
			
		#for item in x:
			fz.write(x + '\n')
if __name__ == "__main__":
	main()
