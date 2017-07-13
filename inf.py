import os
import codecs
import json
import requests
import time
import urllib2
import download_3
from bs4 import BeautifulSoup
def status(link):
	#request = urllib2.Request(link, headers={"Accept" : "text/html"})
	for i in range(2):
		try:
			status = requests.get(link, headers={'Connection':'close'})

		except requests.exceptions.ChunkedEncodingError:
			print("Connection reset by peer!")
			continue

		if status.status_code == 200:
			return status
		else:
			print("link error!")
			time.sleep(0.5)

	else:
		print("ERROR!")
		return False




def get_data_info(link,format):
	print(link)
	ID = link.split("/")[-1]

	r = urllib2.urlopen(link)
	soup = BeautifulSoup(r,"lxml")
	label = soup.find_all("th",class_="field-label")
	value = soup.find_all("td",class_="field-content")
	point = soup.find("span",class_="average-rating")
	text = []
	for i in range(0,len(value)):
		value_text = value[i].get_text()
		new_text = "".join(value_text.split(" "))
	 	label_text = label[i].get_text()
		new = label_text + ": " + new_text
	 	text.append(new)
		path = format + "/" + ID
	 	if os.path.exists(path) == False :
	 		os.makedirs(path)


	with codecs.open( path + "/info.json", 'wb',encoding="utf-8") as outfile:
		outfile.write(unicode(json.dumps(text, ensure_ascii=False)))

	return text



