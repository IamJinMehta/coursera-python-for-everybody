# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("please enter valid file name")
    quit()
    
for line in fh:
    line=line.rstrip()
    print(line.upper())
