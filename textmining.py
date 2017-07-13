# -*- coding: utf-8 -*-
# encoding=utf-8
import jieba
import json
from gensim.models import word2vec
import numpy,scipy

def get_text(path):
	f = open(path)
	x = f.read().split('"')
	#for i in range(1,len(x)-1,2):
	text = []
	for i in range(1,4,2):
		x[i]=x[i].split(": ")[1]
		text.append(x[i])
		print(x[i])
	return text



def main():
	path = 'json/10043/info.json'
	info_text = get_text(path)
	for i in range(0,len(info_text)):
		info_cut = jieba.cut(info_text[i],cut_all=False)
		print(" ".join(info_cut))	
	
if __name__ == "__main__":
    main()
