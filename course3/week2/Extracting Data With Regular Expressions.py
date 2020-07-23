import re
x=input("Enter your file name:")
y=open(x)
a=[]
for line in y:
    z=re.findall('[0-9]+',line)
    a=a+z
s=0
for value in a:
    s=s+int(value)
print(s)



#other way(optional: just for fun)
print(sum([int(i) for i in re.findall('[0-9]+',open(input("Enter your file name:")).read())]))
