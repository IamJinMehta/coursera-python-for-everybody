fname = input("Enter file name: ")
fh = open(fname)
count=0
for line in fh:
    if line.startswith("From"):
        if line.startswith("From:"):
            #print(line)
            continue
        count=count+1
        x=line.split()
        print(x[1])
print("There were", count, "lines in the file with From as the first word")
