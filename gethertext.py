#coding:utf8
import os
import re
import csv
import jieba
import json
import codecs
import sys  


reload(sys)  
sys.setdefaultencoding('utf8')

def get_text(path):
	f = open(path)
	x = f.read().split('"')
	#for i in range(1,len(x)-1,2):
	
	for i in range(1,3,2):
		y=x[i].split(": ")[1]
		
	return y

def utf_8_encoder(unicode_csv_data):
	for line in unicode_csv_data:
		yield line.encode('utf-8')
	
def main():
	text = []
	for id in range(5900,50000):
		path = 'xml/' + str(id) + '/info.json'
		if os.path.exists(path) == True :
			info_text = get_text(path)
			value = '"' + str(id) + '",' + '"' + info_text + '"'
			text.append(value)
			print(value)
			
	with codecs.open( "xml_1.csv", 'w',"utf-8")  as f:
		for item in text:
			f.write(item + '\n')
		f.close()
		
		
		
if __name__ == "__main__":
    main()
