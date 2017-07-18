# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging

def main():
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	sentences = word2vec.Text8Corpus("seg_xml_text.txt")
	model = word2vec.Word2Vec(sentences, size=500,min_count=1,min_alpha=0.0000001)
	model.save("med250.model.bin")

if __name__ == "__main__":
	main()
