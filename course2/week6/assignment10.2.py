fname = input("Enter file name: ")
fh = open(fname)
counts=dict()
icount=0
iword=None
for line in fh:
    if not line.startswith("From:"):
        if line.startswith("From"):
            words=line.split()
            words=words[5]
            words=words.split(':')
            words=words[0]
            counts[words]=counts.get(words,0)+1
l=list()
l=sorted( [ (key,value) for key,value in counts.items() ] )
for key,value in l:
    print(key, value)
