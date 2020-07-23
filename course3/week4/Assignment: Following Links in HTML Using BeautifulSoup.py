import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url=input("Enter URL: ")
count=int(input("Enter count: "))
pos=int(input("Enter position: "))
c=0
def parse(url):
	global c
	if c>count:
		exit()
	else:
		print("Retriving: ",url)
		html=urllib.request.urlopen(url).read()
		soup=BeautifulSoup(html,'html.parser')
		c=c+1
	tags=soup('a')
	cou=0
	for tag in tags:
		url1=tag.get('href',None)
		cou=cou+1
		if cou==pos:
			url=url1
			parse(url)
parse(url)
