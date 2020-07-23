# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("please enter valid file name")
    quit()
    
val=0
count=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        value = line.split(':')[1]
        value = float(value)
        val = val+value
        count = count+1
        
avg=val/count
print("Average spam confidence:",avg)
