import xml.etree.ElementTree as ET
import urllib.request,urllib.error,urllib.parse
url=input("Enter location: ")
read=urllib.request.urlopen(url)
length=read.read()
print("Retrieving ",url)
data=ET.fromstring(length)
lst=data.findall('comments/comment')
c=0
s=0
for item in lst:
    c=c+1
    s=s+int(item.find('count').text)
print("Retrieved",len(length),"characters")
print("Count:",c)
print("Sum:",s)
