fname = input("Enter file name: ")
fh = open(fname)
counts=dict()
icount=0
iword=None
for line in fh:
    if not line.startswith("From:"):
        if line.startswith("From"):
            words=line.split()
            words=words[1]
            counts[words]=counts.get(words,0)+1
for key,value in counts.items():
    if value>icount:
        iword=key
        icount=value
print(iword,icount)
