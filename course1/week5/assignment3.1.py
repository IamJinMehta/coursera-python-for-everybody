hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
try:
    if(h>0 and r>0):
        if(h>float(40)):
            h=h-40
            x=r*h*1.5
            y=40*r
            z=x+y
        else:
            z=h*r
    print(z)
except:
    if(h<0 and r<0):
        print("Hours and Rate must be positive value.")
    elif(h<0):
        print("Hours must be positive value.")
    else:
        print("Rate must be positive value.")
