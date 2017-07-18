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
	y = []	
	#for i in range(1,4,2):
	#print(x[i])
	a=x[1].split(": ")[-1]
	b=x[3].split(": ")[-1]
	y.append(a)
	y.append(b)
	#print(y[0])
	#print(y[1])
	return y

def utf_8_encoder(unicode_csv_data):
	for line in unicode_csv_data:
		yield line.encode('utf-8')
	
def main():
	form = 'json'
	text = []
	text2 = []
	for id in range(5900,50000):
		path = form + '/' + str(id) + '/info.json'
		if os.path.exists(path) == True :
			info_text = get_text(path)
			value = '"' + str(id) + '","' + info_text[0] + '","' + info_text[1] + '"'
			text.append(value)
			print(value)

			value2 = str(id) + " " + info_text[0] #+ " " + info_text[1]
			text2.append(value2)

	with codecs.open( form + ".csv", 'w',"utf-8")  as f:
		for item in text:
			f.write(item + '\n')
		f.close()
		
	with codecs.open( form + ".txt", 'w',"utf-8")  as f:
		for item in text2:
			f.write(item + '\n')
		f.close()
		
if __name__ == "__main__":
    main()
