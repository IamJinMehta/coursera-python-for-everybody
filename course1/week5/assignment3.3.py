score = input("Enter Score: ")
try:
	s=float(score)
except:
    print("please Enter the numeric value")
    quit()

if(s<0 or s>1):
    print("Please Enter value in given range")
elif(s>=0.9):
    print("A")
elif(s>=0.8):
    print("B")
elif(s>=0.7):
    print("C")
elif(s>=0.6):
    print("D")
elif(s<0.6):
    print("F")
else:
    print("Some other Error")
