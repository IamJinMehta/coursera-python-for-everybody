import urllib.request as ure
import urllib.parse as upar
import urllib.error as urror
import json

url=input("Enter location: ")
print('Retrieving',url)
uh=ure.urlopen(url)
data=uh.read().decode()
info=json.loads(data)
print('Retrieved',len(data),'characters')
s=0
c=0
for item in info['comments']:
	c=c+1
	v=item['count']
	s=s+v
print("Count:",c)
print("Sum:",s)
