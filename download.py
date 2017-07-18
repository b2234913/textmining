# -*- coding: UTF-8 -*-
import os 
import sys
import urllib2
import urllib
import requests
import time
import string
import inf
from bs4 import BeautifulSoup

#check status of link 
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



# get link of info 
def get_info_link(link):
	if status(link) != False:
		r = status(link)
		soup = BeautifulSoup(r.text,"lxml")
		r.close()
		a = soup.find_all("td",class_  = "views-field views-field-nothing-3")
		info_link = []
		if info_link != None:
			for i in range(0,len(a)):	
				b = a[i].find("a").get("href")
				b = "http://data.gov.tw" + b 
				info_link.append(b)
			return info_link
		else:
			return

def get_download_link(link,file_format):	
	if status(link) != False:
		r = status(link)

		soup = BeautifulSoup(r.text,"lxml")
		r.close()
		a = soup.find("div",class_="field field-name-field-format-g field-type-taxonomy-term-reference field-label-hidden")
		term = a.get_text()
		if term == file_format.upper():
			b = soup.find("div",class_="field field-name-field-resource-url-g field-type-link-field field-label-hidden")
			download_link = b.get_text()
			return download_link
	

def download_file(link,ID,file_format):
	path = file_format + "/" + str(ID)
	#path = str(ID)
	file_name = path + "/" + str(j) + "." + file_format
	
	if os.path.exists(path) == False :
		os.makedirs(path)
	
	
	r = status(link) 
	with open(file_name, "wb") as code:
	     code.write(r.content)
	#testfile=urllib.URLopener()
	#testfile.retrieve(link,"test.json")
	return

def change(link):
	name = link.split("/")[-1]
	name = urllib2.quote(name.encode('utf-8'))
	newlink = "/".join(link.split("/")[0:-1])+ "/" + name
	return newlink

def check_contain_chinese(check_str):
	for ch in check_str.decode('utf-8'):
		if u'\u4e00' <= ch <= u'\u9fff':
			return True	
	return False
def get_pages(link):
	r = status(link)
	soup = BeautifulSoup(r.text,"lxml")
	r.close()
	a = soup.find_all("li",class_="pager-item")
	pages = []
	index = "http://data.gov.tw/node/"
	for i in range(0,len(a)/2):
		b = a[i].find("a").get("href")
		b = index + b.split("/")[-1]
		pages.append(b)
	return pages

def run(startID,endID):
	file_format = ["json","csv","xml","xls","webservices"]
	for ID in range(startID,endID):
		print(ID)
		index = "http://data.gov.tw/node/"
		link  = index + str(ID)
		if status(link) == False:
			continue

		pages = get_pages(link)	
		pages.insert(0,link)
		print(pages)
				
		global j 
		j = 0
			
		for l in range(0,len(file_format)):
			for k in range(0,len(pages)):
				info_link = get_info_link(pages[k])
				if info_link != None:
					for i in range(0,len(info_link)):
						download_link = get_download_link(info_link[i],file_format[l])
				
				
						if download_link != None:
						
							inf.get_data_info(link,file_format[l])
							j = j + 1
							print(j)
							print(download_link)
							if check_contain_chinese(download_link)==True:
								download_link = change(download_link)
							
							
							try:
								download_link = download_link.encode('utf-8')	
								r = requests.get(download_link, headers={'Connection':'close'},timeout=10)
							except requests.ConnectTimeout:
								print("Download link timeout error!")
								continue							
							except requests.exceptions.RequestException:
								print("Download link error!")
								continue
							except requests.exceptions.ChunkedEncodingError:
								print("Connection reset by peer!")
								time.sleep(0.5)
								continue

							if  status(download_link) == False:
								print("Download_url not good!")		
							else:
								download_file(download_link,ID,file_format[l])




if __name__ == '__main__':
	s = requests.session()
	s.keep_alive = False
	reload(sys)                         # 2
	sys.setdefaultencoding('utf-8')     # 3
	startID = int(sys.argv[1])
	endID = int(sys.argv[2])
	#file_format = sys.argv[3]
	run(startID,endID)



